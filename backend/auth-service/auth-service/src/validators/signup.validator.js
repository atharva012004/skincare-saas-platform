const { z } = require("zod");

const signupSchema = z.object({

    fullName: z
        .string()
        .min(3)
        .max(100),

    email: z
        .string()
        .email(),

    phoneNumber: z
        .string()
        .regex(
            /^[0-9]{10}$/,
            "Phone number must contain 10 digits"
        ),

    password: z
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
            "Must contain a number"
        )
        .regex(
            /[^A-Za-z0-9]/,
            "Must contain special character"
        )
});

module.exports = signupSchema;