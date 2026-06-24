const setRefreshTokenCookie = (
    res,
    token
) => {

    res.cookie(
        "refreshToken",
        token,
        {
            httpOnly: true,

            secure: false,

            sameSite: "lax",

            maxAge:
                7 *
                24 *
                60 *
                60 *
                1000
        }
    );
};

const clearRefreshTokenCookie =
(
    res
) => {

    res.clearCookie(
        "refreshToken"
    );
};

module.exports = {
    setRefreshTokenCookie,
    clearRefreshTokenCookie
};