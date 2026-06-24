const { z } = require("zod");

const changePasswordSchema =
    z.object({

        currentPassword:
            z.string()
                .min(1),

        newPassword:
            z.string()
                .min(8)
                .regex(/[A-Z]/)
                .regex(/[a-z]/)
                .regex(/[0-9]/)
                .regex(/[^A-Za-z0-9]/)
    });

module.exports =
    changePasswordSchema;