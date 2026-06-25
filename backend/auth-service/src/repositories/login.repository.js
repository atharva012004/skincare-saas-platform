const prisma = require("../database/prisma");

class LoginRepository {

    async createLoginHistory(data) {
        return prisma.loginHistory.create({
            data
        });
    }

    async getUserLoginHistory(userId) {
        return prisma.loginHistory.findMany({
            where: {
                userId: BigInt(userId)
            },
            orderBy: {
                loginTime: "desc"
            }
        });
    }
}

module.exports = new LoginRepository();