const userRepository = require(
    "../repositories/user.repository"
);

async function run() {

    const user =
        await userRepository.create({
            fullName: "Atharva Test",

            email: "atharva@test.com",

            phoneNumber: "9999999999",

            passwordHash: "dummyHash"
        });

    console.log(user);
}

run();