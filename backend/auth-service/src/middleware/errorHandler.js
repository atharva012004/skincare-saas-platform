const {
    INTERNAL_SERVER_ERROR
} = require("../constants/statusCodes");

const errorHandler = (
    err,
    req,
    res,
    next
) => {

    const logger =
        require("../utils/logger");

    logger.error({
        message: err.message,
        stack: err.stack
    });

    return res.status(
        err.statusCode || INTERNAL_SERVER_ERROR
    ).json({
        success: false,
        message:
            err.message ||
            "Internal Server Error",

        data: null,

        errors:
            err.errors || null
    });
};

module.exports = errorHandler;