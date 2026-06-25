const authService =
    require("../services/auth.service");

const asyncHandler =
    require("../helpers/asyncHandler");

const {
    successResponse
} = require("../helpers/response.helper");

const {
    CREATED
} = require("../constants/statusCodes");

const {
    USER_REGISTERED,
    LOGIN_SUCCESS,
    PASSWORD_RESET_EMAIL_SENT,
    PASSWORD_RESET_SUCCESS,
    PASSWORD_CHANGED_SUCCESS
} = require(
    "../constants/messages"
);

const {
    setRefreshTokenCookie,
    clearRefreshTokenCookie
} = require(
    "../helpers/cookie.helper"
);

exports.signup =
    asyncHandler(
        async (req, res) => {

            const result =
                await authService.signup(
                    req.validatedData
                );

            return successResponse(
                res,
                CREATED,
                USER_REGISTERED,
                {
                    userId:
                        result.user.id.toString(),

                    email:
                        result.user.email,

                    verificationToken:
                        result.verificationToken
                }
            );
        }
    );

exports.verifyEmail =
    asyncHandler(
        async (req, res) => {

            const { token } =
                req.query;

            await authService
                .verifyEmail(
                    token
                );

            return successResponse(
                res,
                200,
                "Email verified successfully"
            );
        }
    );

exports.login =
    asyncHandler(
        async (req, res) => {

            const result =
                await authService.login(
                    req.validatedData,
                    {
                        ip: req.ip,

                        browser:
                            req.headers[
                            "user-agent"
                            ],

                        device:
                            "Unknown",

                        os:
                            "Unknown"
                    }
                );

            setRefreshTokenCookie(
                res,
                result.refreshToken
            );

            return successResponse(
                res,
                200,
                LOGIN_SUCCESS,
                {
                    accessToken:
                        result.accessToken,

                    user: {
                        id:
                            result.user.id.toString(),

                        email:
                            result.user.email,

                        fullName:
                            result.user.fullName
                    }
                }
            );
        });

exports.refreshToken =
    asyncHandler(
        async (req, res) => {

            const refreshToken =
                req.cookies?.refreshToken ||
                req.body?.refreshToken;

            const result =
                await authService.refreshToken(
                    refreshToken
                );

            setRefreshTokenCookie(
                res,
                result.refreshToken
            );

            return successResponse(
                res,
                200,
                "Token refreshed successfully",
                {
                    accessToken:
                        result.accessToken,

                    refreshToken:
                        result.refreshToken
                }
            );
        }
    );

exports.logout =
    asyncHandler(
        async (req, res) => {

            const refreshToken =
                req.cookies?.refreshToken ||
                req.body?.refreshToken;

            await authService
                .logout(
                    refreshToken
                );

            clearRefreshTokenCookie(
                res
            );

            return successResponse(
                res,
                200,
                "Logout successful"
            );
        });

exports.forgotPassword =
    asyncHandler(
        async (
            req,
            res
        ) => {


            await authService
                .forgotPassword(
                    req.validatedData
                        .email
                );

            return successResponse(
                res,
                200,
                PASSWORD_RESET_EMAIL_SENT
            );
        }
    );

exports.resetPassword =
    asyncHandler(
        async (
            req,
            res
        ) => {


            await authService
                .resetPassword(

                    req.validatedData
                        .token,

                    req.validatedData
                        .newPassword
                );

            return successResponse(
                res,
                200,
                PASSWORD_RESET_SUCCESS
            );
        }
    );

exports.changePassword =
    asyncHandler(
        async (
            req,
            res
        ) => {

            await authService
                .changePassword(

                    req.user.id,

                    req.validatedData
                        .currentPassword,

                    req.validatedData
                        .newPassword
                );

            clearRefreshTokenCookie(
                res
            );

            return successResponse(
                res,
                200,
                PASSWORD_CHANGED_SUCCESS
            );
        }
    );

exports.logoutAll =
    asyncHandler(
        async (
            req,
            res
        ) => {

            await authService
                .logoutAll(
                    req.user.id
                );

            clearRefreshTokenCookie(
                res
            );

            return successResponse(
                res,
                200,
                "Logged out from all devices"
            );
        }
    );

exports.getSessions =
    asyncHandler(
        async (
            req,
            res
        ) => {

            const sessions =
                await authService
                    .getSessions(
                        req.user.id
                    );

            return successResponse(
                res,
                200,
                "Sessions fetched successfully",

                sessions.map(
                    session => ({

                        id:
                            session.id.toString(),

                        createdAt:
                            session.createdAt,

                        expiresAt:
                            session.expiresAt
                    })
                )
            );
        }
    );

exports.revokeSession =
    asyncHandler(
        async (
            req,
            res
        ) => {

            await authService
                .revokeSession(

                    req.user.id,

                    req.params.id
                );

            return successResponse(
                res,
                200,
                "Session revoked successfully"
            );
        }
    );