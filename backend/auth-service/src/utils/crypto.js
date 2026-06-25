const bcrypt = require("bcrypt");
const crypto = require("crypto");

const SALT_ROUNDS = 12;

const hashPassword = async (
    password
) => {

    return bcrypt.hash(
        password,
        SALT_ROUNDS
    );
};

const comparePassword = async (
    password,
    hash
) => {

    return bcrypt.compare(
        password,
        hash
    );
};

const sha256 = (value) => {

    return crypto
        .createHash("sha256")
        .update(value)
        .digest("hex");
};

const generateRandomToken = (
    length = 32
) => {

    return crypto
        .randomBytes(length)
        .toString("hex");
};

module.exports = {
    hashPassword,
    comparePassword,
    sha256,
    generateRandomToken
};