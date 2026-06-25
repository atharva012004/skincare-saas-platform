const { z } = require("zod");

const forgotPasswordSchema =
    z.object({

        email: z
            .string()
            .email()
    });

const resetPasswordSchema =
    z.object({

        token: z
            .string()
            .min(10),

        newPassword: z
            .string()
            .min(
                8,
                "Password must be at least 8 characters"
            )
            .regex(
                /[A-Z]/,
                "Must contain uppercase letter"
            )
            .regex(
                /[a-z]/,
                "Must contain lowercase letter"
            )
            .regex(
                /[0-9]/,
                "Must contain number"
            )
            .regex(
                /[^A-Za-z0-9]/,
                "Must contain special character"
            )
    });

module.exports = {
    forgotPasswordSchema,
    resetPasswordSchema
};