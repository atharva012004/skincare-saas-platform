const fs =
    require("fs");

const path =
    require("path");

function renderTemplate(
    templateName,
    variables = {}
) {


    const templatePath =
        path.join(
            process.cwd(),
            "src",
            "templates",
            templateName
        );

    let html =
        fs.readFileSync(
            templatePath,
            "utf8"
        );

    Object.entries(
        variables
    ).forEach(
        ([key, value]) => {

            html =
                html.replaceAll(
                    `{{${key}}}`,
                    value ?? ""
                );
        }
    );

    return html;


}

module.exports = {
    renderTemplate
};
