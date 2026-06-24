module.exports = {


    User: {

        type: "object",

        properties: {

            id: {
                type: "string",
                example:
                    "64f1a2b3c4d5e6f7a8b9c0d1"
            },

            fullName: {
                type: "string",
                example:
                    "Atharva"
            },

            email: {
                type: "string",
                format: "email",
                example:
                    "atharva@gmail.com"
            },

            phoneNumber: {
                type: "string",
                example:
                    "9876543210"
            }
        }
    },

    LoginRequest: {

        type: "object",

        required: [
            "email",
            "password"
        ],

        properties: {

            email: {
                type: "string",
                format: "email",
                example:
                    "atharva@gmail.com"
            },

            password: {
                type: "string",
                example:
                    "Password@123"
            }
        }
    },

    SignupRequest: {

        type: "object",

        required: [
            "fullName",
            "email",
            "phoneNumber",
            "password"
        ],

        properties: {

            fullName: {
                type: "string",
                example:
                    "Atharva"
            },

            email: {
                type: "string",
                format: "email",
                example:
                    "atharva@gmail.com"
            },

            phoneNumber: {
                type: "string",
                example:
                    "9876543210"
            },

            password: {
                type: "string",
                minLength: 8,
                example:
                    "Password@123"
            }
        }
    },

    SuccessResponse: {

        type: "object",

        properties: {

            success: {
                type: "boolean",
                example: true
            },

            message: {
                type: "string",
                example:
                    "Operation completed successfully"
            },

            data: {
                type: "object",
                nullable: true
            }
        }
    },

    ErrorResponse: {

        type: "object",

        properties: {

            success: {
                type: "boolean",
                example: false
            },

            message: {
                type: "string",
                example:
                    "Something went wrong"
            },

            data: {
                type: "object",
                nullable: true,
                example: null
            },

            errors: {
                type: "array",
                nullable: true,

                items: {
                    type: "string"
                },

                example: [
                    "Field is required",
                    "Invalid format"
                ]
            }
        }
    },

    Session: {

        type: "object",

        properties: {

            id: {
                type: "string",
                example:
                    "sess_64f1a2b3c4d5e6f7"
            },

            device: {
                type: "string",
                example:
                    "Chrome on Windows"
            },

            ipAddress: {
                type: "string",
                example:
                    "192.168.1.1"
            },

            createdAt: {
                type: "string",
                format: "date-time",
                example:
                    "2024-01-15T10:30:00.000Z"
            },

            lastActiveAt: {
                type: "string",
                format: "date-time",
                example:
                    "2024-01-15T12:00:00.000Z"
            }
        }
    }


};