const userRepository =
    require("../repositories/user.repository");

class UserService {

    async getProfile(
        userId
    ) {

        return userRepository.findById(
            userId
        );
    }

    async updateProfile(
        userId,
        data
    ) {

        return userRepository.updateProfile(
            userId,
            data
        );
    }

    async deleteAccount(
        userId
    ) {

        return userRepository.softDelete(
            userId
        );
    }
}

module.exports =
    new UserService();