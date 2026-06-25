const signupSchema =
require("../validators/signup.validator");

const result =
signupSchema.safeParse({

    fullName:
        "Atharva",

    email:
        "atharva@test.com",

    phoneNumber:
        "9999999999",

    password:
        "Password@123"
});

console.log(result);