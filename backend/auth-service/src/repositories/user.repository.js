const prisma = require("../database/prisma");

class UserRepository {

    async findByEmail(email) {
        return prisma.user.findUnique({
            where: {
                email
            }
        });
    }

    async findByPhone(phoneNumber) {
        return prisma.user.findUnique({
            where: {
                phoneNumber
            }
        });
    }

    async findById(id) {
        return prisma.user.findUnique({
            where: {
                id: BigInt(id)
            }
        });
    }

    async create(userData) {
        return prisma.user.create({
            data: userData
        });
    }

    async update(id, data) {
        return prisma.user.update({
            where: {
                id: BigInt(id)
            },
            data
        });
    }

    async verifyEmail(userId) {

        return prisma.user.update({
            where: {
                id: BigInt(userId)
            },
            data: {
                emailVerified: true
            }
        });
    }

    async updateLastLogin(id) {

        return prisma.user.update({
            where: {
                id: BigInt(id)
            },
            data: {
                lastLoginAt:
                    new Date()
            }
        });
    }
    async updateProfile(
        userId,
        data
    ) {

        return prisma.user.update({
            where: {
                id:
                    BigInt(userId)
            },
            data
        });
    }

    async softDelete(
        userId
    ) {

        return prisma.user.update({
            where: {
                id:
                    BigInt(userId)
            },
            data: {

                isActive:
                    false,

                deletedAt:
                    new Date()
            }
        });
    }
}

module.exports = new UserRepository();