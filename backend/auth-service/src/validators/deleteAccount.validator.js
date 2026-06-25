const { z } = require("zod");

const deleteAccountSchema =
    z.object({

        password:
            z.string()
                .min(1)
    });

module.exports =
    deleteAccountSchema;