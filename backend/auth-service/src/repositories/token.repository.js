const prisma =
    require("../database/prisma");

class TokenRepository {

    async create(data) {
        return prisma.refreshToken.create({
            data
        });
    }

    async findRefreshToken(
        tokenHash
    ) {
        return prisma.refreshToken.findFirst({
            where: {
                tokenHash,
                revoked: false
            }
        });
    }

    async revokeToken(id) {
        return prisma.refreshToken.update({
            where: {
                id: BigInt(id)
            },
            data: {
                revoked: true
            }
        });
    }

    async revokeAllUserTokens(
        userId
    ) {
        return prisma.refreshToken.updateMany({
            where: {
                userId:
                    BigInt(userId)
            },
            data: {
                revoked: true
            }
        });
    }

    async getUserSessions(
        userId
    ) {

        return prisma.refreshToken.findMany({

            where: {

                userId:
                    BigInt(userId),

                revoked:
                    false
            },

            orderBy: {

                createdAt:
                    "desc"
            }
        });
    }

    async revokeSession(
        sessionId,
        userId
    ) {

        return prisma.refreshToken.update({

            where: {

                id:
                    BigInt(sessionId)
            },

            data: {

                revoked:
                    true
            }
        });
    }

    async findById(
        id
    ) {

        return prisma.refreshToken.findUnique({

            where: {

                id:
                    BigInt(id)
            }
        });
    }
}

module.exports =
    new TokenRepository();