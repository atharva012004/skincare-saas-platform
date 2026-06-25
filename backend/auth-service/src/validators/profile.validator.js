const { z } =
    require("zod");

const updateProfileSchema =
    z.object({

        fullName:
            z.string()
                .min(2)
                .max(100)
                .optional(),

        phoneNumber:
            z.string()
                .regex(
                    /^[0-9]{10}$/
                )
                .optional()
    });

module.exports = {
    updateProfileSchema
};