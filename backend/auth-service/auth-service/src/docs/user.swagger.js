module.exports = {


    "/users/profile": {

        get: {

            tags: [
                "Users"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Get Profile",

            responses: {

                200: {

                    description:
                        "User profile fetched successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Profile fetched successfully",

                                data: {

                                    id:
                                        "64f1a2b3c4d5e6f7a8b9c0d1",

                                    fullName:
                                        "Atharva",

                                    email:
                                        "atharva@gmail.com",

                                    phoneNumber:
                                        "9876543210"
                                }
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
        },

        put: {

            tags: [
                "Users"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Update Profile",

            requestBody: {

                required: true,

                content: {

                    "application/json": {

                        schema: {

                            type: "object",

                            properties: {

                                fullName: {
                                    type: "string"
                                },

                                phoneNumber: {
                                    type: "string"
                                }
                            }
                        },

                        example: {

                            fullName:
                                "Atharva Updated",

                            phoneNumber:
                                "9123456780"
                        }
                    }
                }
            },

            responses: {

                200: {

                    description:
                        "Profile updated successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Profile updated successfully",

                                data: {

                                    id:
                                        "64f1a2b3c4d5e6f7a8b9c0d1",

                                    fullName:
                                        "Atharva Updated",

                                    email:
                                        "atharva@gmail.com",

                                    phoneNumber:
                                        "9123456780"
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
                                    "Phone number must be 10 digits"
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

    "/users/account": {

        delete: {

            tags: [
                "Users"
            ],

            security: [
                {
                    bearerAuth: []
                }
            ],

            summary:
                "Delete Account",

            responses: {

                200: {

                    description:
                        "Account deleted successfully",

                    content: {

                        "application/json": {

                            example: {

                                success: true,

                                message:
                                    "Account deleted successfully",

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
    }


};