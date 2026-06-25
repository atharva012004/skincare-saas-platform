const ApiError = require("../types/ApiError");
const {
    BAD_REQUEST
} = require("../constants/statusCodes");

const validateRequest = (schema) => {

    if (!schema || typeof schema.safeParse !== "function") {
        throw new Error(
            `validateRequest received an invalid schema: ${schema}. ` +
            `Check that the schema is correctly exported and imported.`
        );
    }

    return (req, res, next) => {

        const result =
            schema.safeParse(req.body);

        if (!result.success) {

            const rawErrors =
                result.error?.errors ?? [];

            const errors =
                rawErrors.map(
                    (error) => ({
                        field:
                            error.path.join("."),
                        message:
                            error.message
                    })
                );

            return next(
                new ApiError(
                    BAD_REQUEST,
                    "Validation failed",
                    errors
                )
            );
        }

        req.validatedData =
            result.data;

        next();
    };
};

module.exports =
    validateRequest;