const express =
    require("express");

const router =
    express.Router();

const authController =
    require("../controllers/auth.controller");

const validateRequest =
    require("../middleware/validateRequest");

const signupSchema =
    require("../validators/signup.validator");

const loginSchema =
    require("../validators/login.validator");

const emailService =
    require("../services/email.service");

const {
    forgotPasswordSchema,
    resetPasswordSchema
} = require(
    "../validators/resetPassword.validator"
);

const changePasswordSchema =
    require(
        "../validators/changePassword.validator"
    );

const authenticateUser =
    require(
        "../middleware/authenticateUser"
    );

router.post(
    "/forgot-password",
    validateRequest(
        forgotPasswordSchema
    ),
    authController.forgotPassword
);

router.post(
    "/reset-password",
    validateRequest(
        resetPasswordSchema
    ),
    authController.resetPassword
);

router.post(
    "/signup",
    validateRequest(
        signupSchema
    ),
    authController.signup
);

router.get(
    "/verify-email",
    authController.verifyEmail
);

router.post(
    "/login",
    validateRequest(
        loginSchema
    ),
    authController.login
);

router.post(
    "/forgot-password",

    validateRequest(
        forgotPasswordSchema
    ),

    authController.forgotPassword
);

router.post(
    "/reset-password",

    validateRequest(
        resetPasswordSchema
    ),

    authController.resetPassword
);


router.post(
    "/refresh-token",
    authController.refreshToken
);

router.post(
    "/logout",
    authController.logout
);

router.post(

    "/logout-all",

    authenticateUser,

    authController.logoutAll
);

router.get(
    "/test-email",

    async (
        req,
        res
    ) => {

        try {

            await emailService
                .sendEmail({

                    to:
                        "test@example.com",

                    subject:
                        "Auth Service Test",

                    html:
                        "<h1>Email Service Working</h1>"
                });

            return res.json({
                success: true,
                message:
                    "Email sent"
            });

        } catch (error) {

            return res.status(500)
                .json({
                    success: false,
                    message:
                        error.message
                });
        }
    }
);

router.get(
    "/smtp-check",

    async (
        req,
        res
    ) => {

        try {

            await emailService
                .verifyConnection();

            return res.json({

                success: true,

                message:
                    "SMTP Connected"
            });

        } catch (error) {

            return res.status(500)
                .json({

                    success: false,

                    message:
                        error.message
                });
        }
    }
);

router.post(

    "/change-password",

    authenticateUser,

    validateRequest(
        changePasswordSchema
    ),

    authController.changePassword
);

router.get(

    "/sessions",

    authenticateUser,

    authController.getSessions
);

router.delete(

    "/sessions/:id",

    authenticateUser,

    authController.revokeSession
);

module.exports = router;