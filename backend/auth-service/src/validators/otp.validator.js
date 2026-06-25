const { z } = require("zod");

const sendOtpSchema = z.object({

    phoneNumber: z
        .string()
        .regex(
            /^[0-9]{10}$/,
            "Invalid phone number"
        )
});

const verifyOtpSchema = z.object({

    phoneNumber: z
        .string()
        .regex(
            /^[0-9]{10}$/
        ),

    otp: z
        .string()
        .length(6)
});

module.exports = {
    sendOtpSchema,
    verifyOtpSchema
};