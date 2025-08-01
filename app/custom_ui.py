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
                    background-color: #041648;
                    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25'%3E%3Cdefs%3E%3ClinearGradient id='a' gradientUnits='userSpaceOnUse' x1='0' x2='0' y1='0' y2='100%25' gradientTransform='rotate(240)'%3E%3Cstop offset='0' stop-color='%23041648'/%3E%3Cstop offset='1' stop-color='%23150235'/%3E%3C/linearGradient%3E%3Cpattern patternUnits='userSpaceOnUse' id='b' width='540' height='450' x='0' y='0' viewBox='0 0 1080 900'%3E%3Cg fill-opacity='0.1'%3E%3Cpolygon fill='%23444' points='90 150 0 300 180 300'/%3E%3Cpolygon points='90 150 180 0 0 0'/%3E%3Cpolygon fill='%23AAA' points='270 150 360 0 180 0'/%3E%3Cpolygon fill='%23DDD' points='450 150 360 300 540 300'/%3E%3Cpolygon fill='%23999' points='450 150 540 0 360 0'/%3E%3Cpolygon points='630 150 540 300 720 300'/%3E%3Cpolygon fill='%23DDD' points='630 150 720 0 540 0'/%3E%3Cpolygon fill='%23444' points='810 150 720 300 900 300'/%3E%3Cpolygon fill='%23FFF' points='810 150 900 0 720 0'/%3E%3Cpolygon fill='%23DDD' points='990 150 900 300 1080 300'/%3E%3Cpolygon fill='%23444' points='990 150 1080 0 900 0'/%3E%3Cpolygon fill='%23DDD' points='90 450 0 600 180 600'/%3E%3Cpolygon points='90 450 180 300 0 300'/%3E%3Cpolygon fill='%23666' points='270 450 180 600 360 600'/%3E%3Cpolygon fill='%23AAA' points='270 450 360 300 180 300'/%3E%3Cpolygon fill='%23DDD' points='450 450 360 600 540 600'/%3E%3Cpolygon fill='%23999' points='450 450 540 300 360 300'/%3E%3Cpolygon fill='%23999' points='630 450 540 600 720 600'/%3E%3Cpolygon fill='%23FFF' points='630 450 720 300 540 300'/%3E%3Cpolygon points='810 450 720 600 900 600'/%3E%3Cpolygon fill='%23DDD' points='810 450 900 300 720 300'/%3E%3Cpolygon fill='%23AAA' points='990 450 900 600 1080 600'/%3E%3Cpolygon fill='%23444' points='990 450 1080 300 900 300'/%3E%3Cpolygon fill='%23222' points='90 750 0 900 180 900'/%3E%3Cpolygon points='270 750 180 900 360 900'/%3E%3Cpolygon fill='%23DDD' points='270 750 360 600 180 600'/%3E%3Cpolygon points='450 750 540 600 360 600'/%3E%3Cpolygon points='630 750 540 900 720 900'/%3E%3Cpolygon fill='%23444' points='630 750 720 600 540 600'/%3E%3Cpolygon fill='%23AAA' points='810 750 720 900 900 900'/%3E%3Cpolygon fill='%23666' points='810 750 900 600 720 600'/%3E%3Cpolygon fill='%23999' points='990 750 900 900 1080 900'/%3E%3Cpolygon fill='%23999' points='180 0 90 150 270 150'/%3E%3Cpolygon fill='%23444' points='360 0 270 150 450 150'/%3E%3Cpolygon fill='%23FFF' points='540 0 450 150 630 150'/%3E%3Cpolygon points='900 0 810 150 990 150'/%3E%3Cpolygon fill='%23222' points='0 300 -90 450 90 450'/%3E%3Cpolygon fill='%23FFF' points='0 300 90 150 -90 150'/%3E%3Cpolygon fill='%23FFF' points='180 300 90 450 270 450'/%3E%3Cpolygon fill='%23666' points='180 300 270 150 90 150'/%3E%3Cpolygon fill='%23222' points='360 300 270 450 450 450'/%3E%3Cpolygon fill='%23FFF' points='360 300 450 150 270 150'/%3E%3Cpolygon fill='%23444' points='540 300 450 450 630 450'/%3E%3Cpolygon fill='%23222' points='540 300 630 150 450 150'/%3E%3Cpolygon fill='%23AAA' points='720 300 630 450 810 450'/%3E%3Cpolygon fill='%23666' points='720 300 810 150 630 150'/%3E%3Cpolygon fill='%23FFF' points='900 300 810 450 990 450'/%3E%3Cpolygon fill='%23999' points='900 300 990 150 810 150'/%3E%3Cpolygon points='0 600 -90 750 90 750'/%3E%3Cpolygon fill='%23666' points='0 600 90 450 -90 450'/%3E%3Cpolygon fill='%23AAA' points='180 600 90 750 270 750'/%3E%3Cpolygon fill='%23444' points='180 600 270 450 90 450'/%3E%3Cpolygon fill='%23444' points='360 600 270 750 450 750'/%3E%3Cpolygon fill='%23999' points='360 600 450 450 270 450'/%3E%3Cpolygon fill='%23666' points='540 600 630 450 450 450'/%3E%3Cpolygon fill='%23222' points='720 600 630 750 810 750'/%3E%3Cpolygon fill='%23FFF' points='900 600 810 750 990 750'/%3E%3Cpolygon fill='%23222' points='900 600 990 450 810 450'/%3E%3Cpolygon fill='%23DDD' points='0 900 90 750 -90 750'/%3E%3Cpolygon fill='%23444' points='180 900 270 750 90 750'/%3E%3Cpolygon fill='%23FFF' points='360 900 450 750 270 750'/%3E%3Cpolygon fill='%23AAA' points='540 900 630 750 450 750'/%3E%3Cpolygon fill='%23FFF' points='720 900 810 750 630 750'/%3E%3Cpolygon fill='%23222' points='900 900 990 750 810 750'/%3E%3Cpolygon fill='%23222' points='1080 300 990 450 1170 450'/%3E%3Cpolygon fill='%23FFF' points='1080 300 1170 150 990 150'/%3E%3Cpolygon points='1080 600 990 750 1170 750'/%3E%3Cpolygon fill='%23666' points='1080 600 1170 450 990 450'/%3E%3Cpolygon fill='%23DDD' points='1080 900 1170 750 990 750'/%3E%3C/g%3E%3C/pattern%3E%3C/defs%3E%3Crect x='0' y='0' fill='url(%23a)' width='100%25' height='100%25'/%3E%3Crect x='0' y='0' fill='url(%23b)' width='100%25' height='100%25'/%3E%3C/svg%3E");
                    background-attachment: fixed;
                    background-size: cover;
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
