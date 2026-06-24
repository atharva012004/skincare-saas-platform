const successResponse = (
    res,
    statusCode,
    message,
    data = null
) => {
    return res.status(statusCode).json({
        success: true,
        message,
        data,
        errors: null
    });
};

const errorResponse = (
    res,
    statusCode,
    message,
    errors = null
) => {
    return res.status(statusCode).json({
        success: false,
        message,
        data: null,
        errors
    });
};

module.exports = {
    successResponse,
    errorResponse
};