const prisma = require("../database/prisma");

class EmailVerificationRepository {

    async create(data) {
        return prisma.emailVerificationToken.create({
            data
        });
    }

    async findByTokenHash(tokenHash) {
        return prisma.emailVerificationToken.findFirst({
            where: {
                tokenHash,
                used: false
            },
            include: {
                user: true
            }
        });
    }

    async markUsed(id) {
        return prisma.emailVerificationToken.update({
            where: {
                id: BigInt(id)
            },
            data: {
                used: true
            }
        });
    }

    async deleteUserTokens(userId) {

        return prisma.emailVerificationToken.deleteMany({
            where: {
                userId: BigInt(userId)
            }
        });
    }
}

module.exports =
    new EmailVerificationRepository();