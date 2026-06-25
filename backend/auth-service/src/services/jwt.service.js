const jwt = require("jsonwebtoken");

const jwtConfig =
    require("../config/jwt.config");

class JwtService {

    generateAccessToken(payload) {

        return jwt.sign(
            payload,
            jwtConfig.accessSecret,
            {
                expiresIn:
                    jwtConfig.accessExpiresIn
            }
        );
    }

    generateRefreshToken(payload) {

        return jwt.sign(
            payload,
            jwtConfig.refreshSecret,
            {
                expiresIn:
                    jwtConfig.refreshExpiresIn
            }
        );
    }

    verifyAccessToken(token) {

        return jwt.verify(
            token,
            jwtConfig.accessSecret
        );
    }

    verifyRefreshToken(token) {

        return jwt.verify(
            token,
            jwtConfig.refreshSecret
        );
    }
}

module.exports =
    new JwtService();