module.exports = {
    content: [
        "./templates/**/*.{html,js}",
        "./home/templates/**/*.{html,js}",
        "./sermons/templates/**/*.{html,js}"
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
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
    ],
};
