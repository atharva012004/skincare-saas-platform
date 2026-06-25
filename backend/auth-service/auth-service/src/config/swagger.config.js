const swaggerJsdoc =
    require(
        "swagger-jsdoc"
    );

const schemas =
    require(
        "../docs/schemas.swagger"
    );

const authDocs =
    require(
        "../docs/auth.swagger"
    );

const userDocs =
    require(
        "../docs/user.swagger"
    );

const options = {


    definition: {

        openapi:
            "3.0.0",

        info: {

            title:
                "Auth Service API",

            version:
                "1.0.0",

            description:
                "Enterprise Authentication Service API Documentation",

            contact: {

                name:
                    "Auth Service Team",

                email:
                    "support@authservice.com"
            }
        },

        servers: [
            {

                url:
                    "http://localhost:5000/api/v1",

                description:
                    "Development Server"
            }
        ],

        tags: [

            {
                name:
                    "Authentication",

                description:
                    "Authentication and Authorization APIs"
            },

            {
                name:
                    "Users",

                description:
                    "User Profile APIs"
            },

            {
                name:
                    "Development",

                description:
                    "Development and Testing APIs"
            }
        ],

        components: {

            securitySchemes: {

                bearerAuth: {

                    type:
                        "http",

                    scheme:
                        "bearer",

                    bearerFormat:
                        "JWT",

                    description:
                        "Enter JWT Access Token"
                }
            },

            schemas
        },

        security: [
            {
                bearerAuth: []
            }
        ],

        paths: {

            ...authDocs,

            ...userDocs
        }
    },

    apis: []


};

const swaggerSpec =
    swaggerJsdoc(
        options
    );

module.exports =
    swaggerSpec;
