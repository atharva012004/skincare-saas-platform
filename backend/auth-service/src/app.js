require("dotenv").config();

const express =
    require("express");

const cors =
    require("cors");

const helmet =
    require("helmet");

const cookieParser =
    require("cookie-parser");

const {
    swaggerUi,
    swaggerSpec
} = require(
    "./swagger"
);

const userRoutes =
    require("./routes/user.routes");

const authRoutes =
    require("./routes/auth.routes");

const errorHandler =
    require(
        "./middleware/errorHandler"
    );

const app =
    express();

app.use(
    helmet()
);

app.use(
    cors()
);

app.use(
    express.json()
);

app.use(
    cookieParser()
);

app.use(


    "/api-docs",

    swaggerUi.serve,

    swaggerUi.setup(
        swaggerSpec
    )


);

app.use(
    "/api/v1/auth",
    authRoutes
);

app.use(
    "/api/v1/users",
    userRoutes
);

app.use(
    errorHandler
);

module.exports =
    app;
