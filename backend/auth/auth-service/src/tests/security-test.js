const {
    hashPassword,
    comparePassword,
    sha256
} = require("../utils/crypto");

async function run() {

    const hash =
        await hashPassword(
            "Password@123"
        );

    console.log(hash);

    const valid =
        await comparePassword(
            "Password@123",
            hash
        );

    console.log(valid);

    console.log(
        sha256("hello")
    );
}

run();