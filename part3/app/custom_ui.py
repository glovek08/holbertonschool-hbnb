def custom_ui(api):
    return (
        '''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>HBnB API Documentation</title>
            <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui.css" />
            <style>
                *, *:before, *:after {
                    -webkit-box-sizing: border-box; 
                    -moz-box-sizing: border-box; 
                    box-sizing: border-box;
                }
                /* Custom Swagger UI Styling */
                * {
                    color: white !important;
                }
                .model-box {
                    width: 80%;
                }
                .swagger-ui .opblock.opblock-get .opblock-summary {
                    background-color: transparent !important;
                }
                body, #swagger-ui, p {
                    # background: #1a1a1a !important;
                    color: #ffffff !important;
                }
                body {
                    background-image: url("https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
                    background-size: cover;
                    background-repeat: no-repeat;
                    padding-top: 80px;
                    padding-bottom: 150px;
                }

                /* Header styling */
                .swagger-ui .topbar {
                    background: #2d2d2d !important;
                    border-bottom: 1px solid #444 !important;
                }

                .swagger-ui .topbar .topbar-wrapper {
                    padding: 10px 0 !important;
                }
                .scheme-container {
                    max-width: 1460px;
                    margin-left: auto !important;
                    margin-right: auto !important;
                }

                /* Main content area */
                .swagger-ui .wrapper {
                    background: #1a1a1a !important;
                    padding: 5px 40px;
                    margin-bottom: 20px;
                    margin-top: 20px;
                }

                /* Operation sections */
                .swagger-ui .opblock {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                    border-radius: 6px !important;
                    margin-bottom: 10px !important;
                }
                svg {
                    filter: invert(100%);
                }
                .swagger-ui .opblock.opblock-put {
                    border-color: #b97623 !important;
                }
                .version {
                    background: green !important;
                }
                ..swagger-ui .info .title small pre {
                    background-color: green !important;
                }
                .model-toggle {
                    filter: invert(100%);
                }
                select {
                    color: black !important;
                }

                .swagger-ui .opblock.opblock-post {
                    border-color: #499551 !important;
                }
                .swagger-ui .opblock.opblock-get {
                    border-color: #1896ec !important;
                }
                .swagger-ui .opblock.opblock-delete {
                    border-color: #ad3e15 !important;
                }

                /* Headers and text */
                .swagger-ui .opblock .opblock-summary {
                    color: #ffffff !important;
                }

                .swagger-ui .opblock-description-wrapper p,
                .swagger-ui .opblock-external-docs-wrapper p,
                .swagger-ui .opblock-title_normal p {
                    color: #ffffff !important;
                }
                
                .swagger-ui .opblock.opblock-post .opblock-summary-method {
                    background: #2c5130 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #66e173 !important;
}
                .swagger-ui .opblock.opblock-get .opblock-summary-method {
                    background: #146fad !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #9e31c4 !important;
}
                .swagger-ui .opblock.opblock-put .opblock-summary-method {
                    background: #595117 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #cfbd35 !important;
}
                .swagger-ui .opblock.opblock-delete .opblock-summary-method {
                    background: #591b17 !important;
                    color: #ffffff !important;
                    font-weight: bold !important;
                    border-radius: 3px !important;
                    padding: 2px 6px !important;
                    border-color: #da3025 !important;
}
                
                .opblock-section-header {
                    background: black !important;
                }

                /* Response section */
                .swagger-ui .responses-wrapper {
                    background: #2d2d2d !important;
                }

                /* Input fields */
                .swagger-ui .parameters-col_description input,
                .swagger-ui .parameters-col_description select,
                .swagger-ui textarea {
                    background: #383838 !important;
                    color: #ffffff !important;
                    border: 1px solid #555 !important;
                }

                /* Buttons */
                .swagger-ui .btn {
                    color: #ffffff !important;
                    border: none !important;
                }

                .swagger-ui .btn:hover {
                    background: #4e90d9 !important;
                }

                /* Models section */
                .swagger-ui .model-box {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                }

                /* MODAL AUTHORIZE! */
                .swagger-ui .dialog-ux .modal-ux {
                    background: #1c1a1a !important;
                }

                .swagger-ui .auth-wrapper .authorize {
                    background-color: #205039 !important;
                    margin: 5px 10px;
                }
                .swagger-ui .auth-wrapper .authorize:hover {
                    background-color: darkgreen !important;
                }
                .swagger-ui .auth-wrapper .btn.modal-btn.auth.btn-done {
                background-color: darkred !important;
                color: white !important;
                border: 1px solid #666 !important;
                }

                .swagger-ui .auth-wrapper::before {
                    content: "Include JWT token in header for maximum control 😎👉 (Append `Bearer`)";
                    display: block;
                    color: #ffffff !important;
                    font-size: 14px;
                    font-weight: bold;
                    padding: 8px 12px;
                    margin-top: auto;
                    margin-bottom: auto;
                    border-radius: 4px;
                    text-align: center;
                }

                .swagger-ui .auth-wrapper .btn.modal-btn.auth.btn-done:hover {
                background-color: red !important;
                border-color: #999 !important;
                }

                .auth-container input {
                    color: black !important;
                }

                .swagger-ui .model .property {
                    color: #ffffff !important;
                }

                /* Additional dark theme improvements */
                .swagger-ui .info {
                    color: #ffffff !important;
                    margin: 20px;
                }

                .swagger-ui .info .title {
                    color: #ffffff !important;
                }

                .swagger-ui .scheme-container {
                    background: #2d2d2d !important;
                    border: 1px solid #444 !important;
                }

                .swagger-ui .tab li {
                    color: #ffffff !important;
                }

                .swagger-ui .opblock-summary-path {
                    color: #ffffff !important;
                }
            </style>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui-bundle.js"></script>
            <script>
                window.onload = function() {
                    const ui = SwaggerUIBundle({
                        url: "'''
        + api.base_url
        + """swagger.json",
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIBundle.presets.standalone
                        ],
                        layout: "BaseLayout"
                    });
                };
            </script>
        </body>
        </html>
        """
    )
