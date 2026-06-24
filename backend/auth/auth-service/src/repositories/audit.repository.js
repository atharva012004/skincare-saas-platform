const prisma = require("../database/prisma");

class AuditRepository {

    async create(data) {
        return prisma.auditLog.create({
            data
        });
    }
}

module.exports = new AuditRepository();