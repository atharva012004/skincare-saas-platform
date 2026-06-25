const nodemailer =
    require("nodemailer");

const fs =
    require("fs");

const path =
    require("path");

const mailConfig =
    require("../config/mail.config");

const {
    renderTemplate
} = require(
    "../helpers/template.helper"
);

class EmailService {


    constructor() {

        this.transporter =
            nodemailer.createTransport({

                host:
                    mailConfig.host,

                port:
                    mailConfig.port,

                secure:
                    false,

                auth: {

                    user:
                        mailConfig.user,

                    pass:
                        mailConfig.password
                }
            });
    }

    async verifyConnection() {

        return this.transporter.verify();
    }

    async sendEmail({
        to,
        subject,
        html
    }) {

        return this.transporter.sendMail({

            from:
                mailConfig.from,

            to,

            subject,

            html
        });
    }

    loadTemplate(
        templateName
    ) {

        const templatePath =
            path.join(
                process.cwd(),
                "src",
                "templates",
                templateName
            );

        return fs.readFileSync(
            templatePath,
            "utf8"
        );
    }

    async sendPasswordResetEmail({

        to,

        fullName,

        resetUrl

    }) {

        let html =
            this.loadTemplate(
                "reset-password.html"
            );

        html =
            html.replace(
                /{{fullName}}/g,
                fullName
            );

        html =
            html.replace(
                /{{resetUrl}}/g,
                resetUrl
            );

        return this.sendEmail({

            to,

            subject:
                "Reset Your Password",

            html
        });
    }

    async sendWelcomeEmail({


        to,

        fullName

    }) {


        let html =
            this.loadTemplate(
                "welcome.html"
            );

        html =
            html.replace(
                /{{fullName}}/g,
                fullName
            );

        return this.sendEmail({

            to,

            subject:
                "Welcome to Auth Service",

            html
        });

    }

}

module.exports =
    new EmailService();
