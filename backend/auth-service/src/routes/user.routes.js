const express =
    require("express");

const router =
    express.Router();

const userController =
    require("../controllers/user.controller");

const authenticateUser =
    require("../middleware/authenticateUser");

router.get(
    "/profile",
    authenticateUser,
    userController.getProfile
);

router.put(
    "/profile",
    authenticateUser,
    userController.updateProfile
);

router.delete(
    "/account",
    authenticateUser,
    userController.deleteAccount
);

module.exports =
    router;