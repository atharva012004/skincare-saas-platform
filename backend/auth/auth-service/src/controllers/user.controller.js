const asyncHandler =
    require("../helpers/asyncHandler");

const {
    successResponse
} = require("../helpers/response.helper");

const userService =
    require("../services/user.service");

exports.getProfile =
    asyncHandler(
        async (
            req,
            res
        ) => {

            const user =
                await userService.getProfile(
                    req.user.id
                );

            return successResponse(
                res,
                200,
                "Profile fetched successfully",
                {
                    id:
                        user.id.toString(),

                    fullName:
                        user.fullName,

                    email:
                        user.email,

                    phoneNumber:
                        user.phoneNumber,

                    role:
                        user.role,

                    emailVerified:
                        user.emailVerified
                }
            );
        }
    );

exports.updateProfile =
    asyncHandler(
        async (
            req,
            res
        ) => {

            const user =
                await userService
                    .updateProfile(
                        req.user.id,
                        req.body
                    );

            return successResponse(
                res,
                200,
                "Profile updated successfully",
                {
                    id:
                        user.id.toString(),

                    fullName:
                        user.fullName,

                    email:
                        user.email,

                    phoneNumber:
                        user.phoneNumber
                }
            );
        }
    );

exports.deleteAccount =
    asyncHandler(
        async (
            req,
            res
        ) => {

            await userService
                .deleteAccount(
                    req.user.id
                );

            return successResponse(
                res,
                200,
                "Account deleted successfully"
            );
        }
    );