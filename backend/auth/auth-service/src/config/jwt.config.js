const config = {

    accessSecret:
        process.env.JWT_ACCESS_SECRET,

    refreshSecret:
        process.env.JWT_REFRESH_SECRET,

    accessExpiresIn:
        process.env.JWT_ACCESS_EXPIRES || "15m",

    refreshExpiresIn:
        process.env.JWT_REFRESH_EXPIRES || "7d"
};

if (!config.accessSecret) {
    throw new Error(
        "JWT_ACCESS_SECRET missing"
    );
}

if (!config.refreshSecret) {
    throw new Error(
        "JWT_REFRESH_SECRET missing"
    );
}

module.exports = config;