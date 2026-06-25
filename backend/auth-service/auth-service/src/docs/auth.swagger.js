module.exports = {

    "/auth/signup": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Register User",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            $ref:
                                "#/components/schemas/SignupRequest"
                        },

                        example: {

                            fullName:
                                "Atharva",

                            email:
                                "atharva@gmail.com",

                            phoneNumber:
                                "9876543210",

                            password:
                                "Password@123"
                        }
                    }
                }
            },

            responses: {

                201: {

                    description:
                        "User registered successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "User registered successfully. Please verify your email.",

                                data: {

                                    id:
                                        "64f1a2b3c4d5e6f7a8b9c0d1",

                                    fullName:
                                        "Atharva",

                                    email:
                                        "atharva@gmail.com"
                                }
                            }
                        }
                    }
                },

                400: {

                    description:
                        "Validation error",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Validation failed",

                                errors: [
                                    "Email is required",
                                    "Password must be at least 8 characters"
                                ]
                            }
                        }
                    }
                },

                409: {

                    description:
                        "Email already in use",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "An account with this email already exists",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/verify-email": {

        get: {

            tags: [
                "Authentication"
            ],

            summary:
                "Verify User Email",

            parameters: [

                {
                    in: "query",
                    name: "token",
                    required: true,

                    schema: {
                        type: "string"
                    },

                    example:
                        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",

                    description:
                        "Email verification token sent to the user's email"
                }
            ],

            responses: {

                200: {

                    description:
                        "Email verified successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Email verified successfully",

                                data: null
                            }
                        }
                    }
                },

                400: {

                    description:
                        "Invalid or expired token",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Verification token is invalid or has expired",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/login": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Login User",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            $ref:
                                "#/components/schemas/LoginRequest"
                        },

                        example: {

                            email:
                                "atharva@gmail.com",

                            password:
                                "Password@123"
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Login successful",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Login successful",

                                data: {

                                    accessToken:
                                        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",

                                    refreshToken:
                                        "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...",

                                    user: {

                                        id:
                                            "64f1a2b3c4d5e6f7a8b9c0d1",

                                        fullName:
                                            "Atharva",

                                        email:
                                            "atharva@gmail.com"
                                    }
                                }
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Invalid credentials",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Invalid email or password",

                                data: null
                            }
                        }
                    }
                },

                403: {

                    description:
                        "Email not verified",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Please verify your email before logging in",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/forgot-password": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Forgot Password",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            required: [
                                "email"
                            ],

                            properties: {

                                email: {
                                    type: "string",
                                    format: "email"
                                }
                            }
                        },

                        example: {

                            email:
                                "atharva@gmail.com"
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Password reset email sent",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Password reset email sent if an account with that email exists",

                                data: null
                            }
                        }
                    }
                },

                400: {

                    description:
                        "Validation error",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Please provide a valid email address",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/reset-password": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Reset Password",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            required: [
                                "token",
                                "password"
                            ],

                            properties: {

                                token: {
                                    type: "string"
                                },

                                password: {
                                    type: "string",
                                    minLength: 8
                                }
                            }
                        },

                        example: {

                            token:
                                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",

                            password:
                                "NewPassword@456"
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Password reset successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Password has been reset successfully",

                                data: null
                            }
                        }
                    }
                },

                400: {

                    description:
                        "Invalid or expired token",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Password reset token is invalid or has expired",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/refresh-token": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Refresh Access Token",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            required: [
                                "refreshToken"
                            ],

                            properties: {

                                refreshToken: {
                                    type: "string"
                                }
                            }
                        },

                        example: {

                            refreshToken:
                                "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "New access token issued",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Token refreshed successfully",

                                data: {

                                    accessToken:
                                        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
                                }
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Invalid or expired refresh token",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Refresh token is invalid or has expired",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/logout": {

        post: {

            tags: [
                "Authentication"
            ],

            summary:
                "Logout",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            required: [
                                "refreshToken"
                            ],

                            properties: {

                                refreshToken: {
                                    type: "string"
                                }
                            }
                        },

                        example: {

                            refreshToken:
                                "dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4..."
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Logged out successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Logged out successfully",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/logout-all": {

        post: {

            tags: [
                "Authentication"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Logout All Devices",

            responses: {

                200: {

                    description:
                        "All sessions revoked",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Logged out from all devices successfully",

                                data: null
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Unauthorized",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Access token is missing or invalid",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/change-password": {

        post: {

            tags: [
                "Authentication"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Change Password",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            required: [
                                "currentPassword",
                                "newPassword"
                            ],

                            properties: {

                                currentPassword: {
                                    type: "string"
                                },

                                newPassword: {
                                    type: "string",
                                    minLength: 8
                                }
                            }
                        },

                        example: {

                            currentPassword:
                                "Password@123",

                            newPassword:
                                "NewPassword@456"
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Password changed successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Password changed successfully",

                                data: null
                            }
                        }
                    }
                },

                400: {

                    description:
                        "Validation error or incorrect current password",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Current password is incorrect",

                                data: null
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Unauthorized",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Access token is missing or invalid",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/sessions": {

        get: {

            tags: [
                "Authentication"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Get Active Sessions",

            responses: {

                200: {

                    description:
                        "List of active sessions",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Sessions fetched successfully",

                                data: [

                                    {
                                        id:
                                            "sess_64f1a2b3c4d5e6f7",

                                        device:
                                            "Chrome on Windows",

                                        ipAddress:
                                            "192.168.1.1",

                                        createdAt:
                                            "2024-01-15T10:30:00.000Z",

                                        lastActiveAt:
                                            "2024-01-15T12:00:00.000Z"
                                    },

                                    {
                                        id:
                                            "sess_a8b9c0d1e2f3a4b5",

                                        device:
                                            "Safari on iPhone",

                                        ipAddress:
                                            "10.0.0.5",

                                        createdAt:
                                            "2024-01-14T08:00:00.000Z",

                                        lastActiveAt:
                                            "2024-01-15T09:45:00.000Z"
                                    }
                                ]
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Unauthorized",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Access token is missing or invalid",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/sessions/{id}": {

        delete: {

            tags: [
                "Authentication"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Revoke Specific Session",

            parameters: [

                {
                    in: "path",
                    name: "id",
                    required: true,

                    schema: {
                        type: "string"
                    },

                    example:
                        "sess_64f1a2b3c4d5e6f7",

                    description:
                        "The ID of the session to revoke"
                }
            ],

            responses: {

                200: {

                    description:
                        "Session revoked successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Session revoked successfully",

                                data: null
                            }
                        }
                    }
                },

                401: {

                    description:
                        "Unauthorized",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Access token is missing or invalid",

                                data: null
                            }
                        }
                    }
                },

                404: {

                    description:
                        "Session not found",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Session not found or already revoked",

                                data: null
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/test-email": {

        get: {

            tags: [
                "Development"
            ],

            summary:
                "Send Test Email",

            responses: {

                200: {

                    description:
                        "Test email sent successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Email sent"
                            }
                        }
                    }
                },

                500: {

                    description:
                        "Email service error",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "Connection refused: SMTP server not reachable"
                            }
                        }
                    }
                }
            }
        }
    },

    "/auth/smtp-check": {

        get: {

            tags: [
                "Development"
            ],

            summary:
                "Verify SMTP Connection",

            responses: {

                200: {

                    description:
                        "SMTP connection is healthy",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "SMTP Connected"
                            }
                        }
                    }
                },

                500: {

                    description:
                        "SMTP connection failed",

                    content: {

                        "application/json": {

                            example: {

                                success: false,

                                message:
                                    "ECONNREFUSED: Unable to connect to SMTP server"
                            }
                        }
                    }
                }
            }
        }
    }

};