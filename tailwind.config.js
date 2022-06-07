module.exports = {
    content: [
        "./templates/**/*.{html,js}",
        "./home/templates/**/*.{html,js}",
        "./sermons/templates/**/*.{html,js}",
        "./streams/templates/**/*.{html,js}",
        "./contactus/templates/**/*.{html,js}",
    ],
    safelist: [
        "tailwind-input",
        "tailwind-input-label",
        "tailwind-checkbox",
    ],
    theme: {
        extend: {
            backgroundImage: {
                "background-pattern": "url('/static/img/background.svg')",
                "hero-background": "url('/static/img/hero-texture-33-4.jpg')",
            },
            colors: {
                primary: {
                    "default": "#602627",
                    "shade": "#4d1d1e",
                    "tint": "#7b3a3b",
                },
                secondary: {
                    "default": "#26605f",
                    "shade": "#1d4d4e",
                    "tint": "#3b7b7c",

                },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
};
