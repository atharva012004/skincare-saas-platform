const jwtService =
    require("../services/jwt.service");

const userRepository =
    require("../repositories/user.repository");

const ApiError =
    require("../types/ApiError");

module.exports =
    async (
        req,
        res,
        next
    ) => {

        try {

            const authHeader =
                req.headers.authorization;

            if (
                !authHeader ||
                !authHeader.startsWith(
                    "Bearer "
                )
            ) {

                throw new ApiError(
                    401,
                    "Authentication required"
                );
            }

            const token =
                authHeader.split(" ")[1];

            const decoded =
                jwtService.verifyAccessToken(
                    token
                );

            const user =
                await userRepository.findById(
                    decoded.userId
                );

            if (!user) {

                throw new ApiError(
                    401,
                    "User not found"
                );
            }

            if (!user.isActive) {

                throw new ApiError(
                    403,
                    "Account disabled"
                );
            }

            req.user = {
                id: user.id,
                email: user.email,
                role: user.role
            };

            next();

        } catch (error) {

            next(error);
        }
    };