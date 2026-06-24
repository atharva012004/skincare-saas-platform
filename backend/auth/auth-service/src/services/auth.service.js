const userRepository =
    require("../repositories/user.repository");

const auditRepository =
    require("../repositories/audit.repository");

const emailVerificationRepository =
    require("../repositories/emailVerification.repository");

const tokenRepository =
    require("../repositories/token.repository");

const loginRepository =
    require("../repositories/login.repository");

const jwtService =
    require("./jwt.service");

const ApiError =
    require("../types/ApiError");

const {
    CONFLICT,
    UNAUTHORIZED,
    FORBIDDEN,
    BAD_REQUEST
} = require("../constants/statusCodes");

const {
    EMAIL_ALREADY_EXISTS,
    PHONE_ALREADY_EXISTS,
    INVALID_CREDENTIALS,
    EMAIL_NOT_VERIFIED,
    ACCOUNT_DISABLED,
    EMAIL_ALREADY_VERIFIED,
    INVALID_VERIFICATION_TOKEN,
    VERIFICATION_TOKEN_EXPIRED,
    INVALID_RESET_TOKEN,
    RESET_TOKEN_EXPIRED,
    CURRENT_PASSWORD_INCORRECT
} = require("../constants/messages");

const {
    hashPassword,
    comparePassword,
    generateRandomToken,
    sha256
} = require("../utils/crypto");

const passwordResetRepository =
    require("../repositories/passwordReset.repository");

const emailService =
    require("./email.service");

class AuthService {

    async signup(data) {

        const existingEmail =
            await userRepository.findByEmail(
                data.email
            );

        if (existingEmail) {
            throw new ApiError(
                CONFLICT,
                EMAIL_ALREADY_EXISTS
            );
        }

        const existingPhone =
            await userRepository.findByPhone(
                data.phoneNumber
            );

        if (existingPhone) {
            throw new ApiError(
                CONFLICT,
                PHONE_ALREADY_EXISTS
            );
        }

        const passwordHash =
            await hashPassword(
                data.password
            );

        const user =
            await userRepository.create({
                fullName:
                    data.fullName,

                email:
                    data.email,

                phoneNumber:
                    data.phoneNumber,

                passwordHash,

                emailVerified:
                    false,

                role:
                    "USER"
            });

        const rawToken =
            generateRandomToken();

        const tokenHash =
            sha256(rawToken);

        await emailVerificationRepository.create({
            userId:
                user.id,

            tokenHash,

            expiresAt:
                new Date(
                    Date.now() +
                    24 * 60 * 60 * 1000
                )
        });

        await auditRepository.create({
            userId:
                user.id,

            action:
                "USER_REGISTERED",

            metadata: {
                email:
                    user.email
            }
        });

        return {
            user,
            verificationToken:
                rawToken
        };
    }

    async verifyEmail(token) {

        const tokenHash =
            sha256(token);

        const record =
            await emailVerificationRepository
                .findByTokenHash(
                    tokenHash
                );

        if (!record) {
            throw new ApiError(
                BAD_REQUEST,
                INVALID_VERIFICATION_TOKEN
            );
        }

        if (
            record.expiresAt <
            new Date()
        ) {
            throw new ApiError(
                BAD_REQUEST,
                VERIFICATION_TOKEN_EXPIRED
            );
        }

        if (
            record.user.emailVerified
        ) {
            throw new ApiError(
                BAD_REQUEST,
                EMAIL_ALREADY_VERIFIED
            );
        }

        await userRepository.verifyEmail(
            record.user.id
        );

        await emailService.sendWelcomeEmail({

            to:
                record.user.email,

            fullName:
                record.user.fullName
        });

        await emailVerificationRepository.markUsed(
            record.id
        );

        await emailVerificationRepository.deleteUserTokens(
            record.user.id
        );

        await auditRepository.create({


            userId:
                record.user.id,

            action:
                "EMAIL_VERIFIED",

            metadata: {

                email:
                    record.user.email
            }


        });


        return true;
    }

    async login(
        data,
        requestInfo
    ) {

        const user =
            await userRepository.findByEmail(
                data.email
            );

        if (!user) {
            throw new ApiError(
                UNAUTHORIZED,
                INVALID_CREDENTIALS
            );
        }

        if (
            !user.emailVerified
        ) {
            throw new ApiError(
                FORBIDDEN,
                EMAIL_NOT_VERIFIED
            );
        }

        if (
            !user.isActive
        ) {
            throw new ApiError(
                FORBIDDEN,
                ACCOUNT_DISABLED
            );
        }

        const passwordMatched =
            await comparePassword(
                data.password,
                user.passwordHash
            );

        if (!passwordMatched) {
            throw new ApiError(
                UNAUTHORIZED,
                INVALID_CREDENTIALS
            );
        }

        const payload = {

            userId:
                user.id.toString(),

            email:
                user.email,

            role:
                user.role,

            tenantId:
                user.tenantId || null,

            merchantId:
                user.merchantId || null,

            userType:
                user.userType || "PLATFORM"
        };

        const accessToken =
            jwtService
                .generateAccessToken(
                    payload
                );

        const refreshToken =
            jwtService
                .generateRefreshToken(
                    payload
                );

        await tokenRepository.create({
            userId:
                user.id,

            tokenHash:
                sha256(
                    refreshToken
                ),

            expiresAt:
                new Date(
                    Date.now() +
                    7 * 24 * 60 * 60 * 1000
                )
        });

        await userRepository.updateLastLogin(
            user.id
        );

        await loginRepository.createLoginHistory({
            userId:
                user.id,

            ipAddress:
                requestInfo.ip,

            browser:
                requestInfo.browser,

            device:
                requestInfo.device,

            os:
                requestInfo.os
        });

        await auditRepository.create({
            userId:
                user.id,

            action:
                "LOGIN_SUCCESS",

            metadata: {
                ip:
                    requestInfo.ip
            }
        });

        return {
            accessToken,
            refreshToken,
            user
        };
    }

    async refreshToken(
        refreshToken
    ) {

        const decoded =
            jwtService
                .verifyRefreshToken(
                    refreshToken
                );

        const tokenHash =
            sha256(
                refreshToken
            );

        const storedToken =
            await tokenRepository
                .findRefreshToken(
                    tokenHash
                );

        if (!storedToken) {

            throw new ApiError(
                401,
                "Invalid refresh token"
            );
        }

        if (
            storedToken.expiresAt <
            new Date()
        ) {

            throw new ApiError(
                401,
                "Refresh token expired"
            );
        }

        await tokenRepository
            .revokeToken(
                storedToken.id
            );

        const payload = {

            userId:
                decoded.userId,

            email:
                decoded.email,

            role:
                decoded.role,

            tenantId:
                decoded.tenantId || null,

            merchantId:
                decoded.merchantId || null,

            userType:
                decoded.userType || "PLATFORM"
        };

        const newAccessToken =
            jwtService
                .generateAccessToken(
                    payload
                );

        const newRefreshToken =
            jwtService
                .generateRefreshToken(
                    payload
                );

        await tokenRepository.create({

            userId:
                BigInt(
                    decoded.userId
                ),

            tokenHash:
                sha256(
                    newRefreshToken
                ),

            expiresAt:
                new Date(
                    Date.now() +
                    7 *
                    24 *
                    60 *
                    60 *
                    1000
                )
        });

        return {
            accessToken:
                newAccessToken,

            refreshToken:
                newRefreshToken
        };
    }

    async logout(
        refreshToken
    ) {

        const tokenHash =
            sha256(
                refreshToken
            );

        const storedToken =
            await tokenRepository
                .findRefreshToken(
                    tokenHash
                );

        if (storedToken) {

            await tokenRepository
                .revokeToken(
                    storedToken.id
                );
        }

        return true;
    }

    async forgotPassword(email) {


        const user =
            await userRepository.findByEmail(
                email
            );

        if (!user) {

            return true;
        }

        const rawToken =
            generateRandomToken();

        console.log(
            "RESET TOKEN:",
            rawToken
        );

        const tokenHash =
            sha256(rawToken);

        await passwordResetRepository
            .deleteUserTokens(
                user.id
            );

        await passwordResetRepository
            .create({

                userId:
                    user.id,

                tokenHash,

                expiresAt:
                    new Date(
                        Date.now() +
                        60 * 60 * 1000
                    )
            });

        const resetUrl =
            `http://localhost:3000/reset-password?token=${rawToken}`;

        await emailService
            .sendPasswordResetEmail({

                to:
                    user.email,

                fullName:
                    user.fullName,

                resetUrl
            });

        return true;

    }

    async resetPassword(
        token,
        newPassword
    ) {

        const tokenHash =
            sha256(token);

        const record =
            await passwordResetRepository
                .findByTokenHash(
                    tokenHash
                );

        if (!record) {

            throw new ApiError(
                BAD_REQUEST,
                INVALID_RESET_TOKEN
            );
        }

        if (
            record.expiresAt <
            new Date()
        ) {

            throw new ApiError(
                BAD_REQUEST,
                RESET_TOKEN_EXPIRED
            );
        }

        const passwordHash =
            await hashPassword(
                newPassword
            );

        await userRepository.update(
            record.user.id,
            {
                passwordHash
            }
        );

        await passwordResetRepository
            .markUsed(
                record.id
            );

        await passwordResetRepository
            .deleteUserTokens(
                record.user.id
            );

        await tokenRepository
            .revokeAllUserTokens(
                record.user.id
            );

        await auditRepository.create({

            userId:
                record.user.id,

            action:
                "PASSWORD_RESET",

            metadata: {

                email:
                    record.user.email
            }
        });

        return true;
    }

    async changePassword(
        userId,
        currentPassword,
        newPassword
    ) {

        const user =
            await userRepository.findById(
                userId
            );

        const passwordMatched =
            await comparePassword(
                currentPassword,
                user.passwordHash
            );

        if (!passwordMatched) {

            throw new ApiError(
                BAD_REQUEST,
                CURRENT_PASSWORD_INCORRECT
            );
        }

        const passwordHash =
            await hashPassword(
                newPassword
            );

        await userRepository.update(
            user.id,
            {
                passwordHash
            }
        );

        await tokenRepository
            .revokeAllUserTokens(
                user.id
            );

        await auditRepository.create({

            userId:
                user.id,

            action:
                "PASSWORD_CHANGED",

            metadata: {}
        });

        return true;
    }

    async logoutAll(
        userId
    ) {

        await tokenRepository
            .revokeAllUserTokens(
                userId
            );

        await auditRepository.create({

            userId:
                BigInt(userId),

            action:
                "LOGOUT_ALL_DEVICES",

            metadata: {}
        });

        return true;
    }

    async getSessions(
        userId
    ) {

        return tokenRepository
            .getUserSessions(
                userId
            );
    }

    async revokeSession(
        userId,
        sessionId
    ) {

        const session =
            await tokenRepository
                .findById(
                    sessionId
                );

        console.log("SESSION:", session);

        console.log(
            "SESSION USER ID:",
            session.userId
        );

        console.log(
            "REQUEST USER ID:",
            userId
        );

        console.log(
            "SESSION USER STRING:",
            session.userId.toString()
        );

        console.log(
            "REQUEST USER STRING:",
            userId.toString()
        );

        if (!session) {

            throw new ApiError(
                BAD_REQUEST,
                "Session not found"
            );
        }

        if (
            session.userId.toString() !==
            userId.toString()
        ) {

            throw new ApiError(
                FORBIDDEN,
                "Access denied"
            );
        }

        await tokenRepository
            .revokeSession(

                sessionId,

                userId
            );

        await auditRepository.create({

            userId:
                BigInt(userId),

            action:
                "SESSION_REVOKED",

            metadata: {

                sessionId
            }
        });

        return true;
    }
}

module.exports =
    new AuthService();