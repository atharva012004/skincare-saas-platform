const prisma =
    require("../database/prisma");

class PasswordResetRepository {

    async create(data) {

        return prisma.passwordResetToken.create({
            data
        });
    }

    async findByTokenHash(
        tokenHash
    ) {

        return prisma.passwordResetToken.findFirst({

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

        return prisma.passwordResetToken.update({

            where: {
                id: BigInt(id)
            },

            data: {
                used: true
            }
        });
    }

    async deleteUserTokens(
        userId
    ) {

        return prisma.passwordResetToken.deleteMany({

            where: {
                userId: BigInt(userId)
            }
        });
    }
}

module.exports =
    new PasswordResetRepository();