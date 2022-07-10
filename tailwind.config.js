module.exports = {
    content: [
        "./templates/**/*.{html,js}",
        "./accounts/templates/**/*.{html,js}",
        "./home/templates/**/*.{html,js}",
        "./schedules/templates/**/*.{html,js}",
        "./sermons/templates/**/*.{html,js}",
        "./streams/templates/**/*.{html,js}",
        "./contactus/templates/**/*.{html,js}",
    ],
    safelist: [
        "input",
        "input-bordered",
        "select",
        "select-bordered",
        "select-multiple",
        "toggle",
        "toggle-primary",
        "w-full",
        "max-w-xs",
        "max-w-sm",
        "textarea",
        "textarea-bordered",
        "h-20",
        "alert-info",
        "alert-success",
        "alert-warning",
        "alert-error",
    ],
    theme: {
        extend: {
            backgroundImage: {
                "background-pattern": "url('/static/img/background.svg')",
                "hero-background": "url('/static/img/hero-texture-33-4.jpg')",
            },
            // colors: {
            //     primary: {
            //         "default": "#602627",
            //         "shade": "#4d1d1e",
            //         "tint": "#7b3a3b",
            //     },
            //     secondary: {
            //         "default": "#26605f",
            //         "shade": "#1d4d4e",
            //         "tint": "#3b7b7c",
            //
            //     },
            // },
        },
    },
    daisyui: {
        themes: [
            {
                mgtheme: {
                    "primary": "#602627",
                    "primary-content": "#fbffff",
                    "secondary": "#e45126",
                    "accent": "#3c7693",
                    "neutral": "#271C27",
                    "base-100": "#fffeff",
                    "base-200": "#f5f5f5",
                    "base-300": "#ebebeb",
                    "info": "#5590D8",
                    "success": "#36CE85",
                    "warning": "#D77409",
                    "error": "#EC2233",
                },
            },
        ],
    },
    plugins: [
        require("daisyui"),
    ],
};
