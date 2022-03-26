module.exports = {
  content: ["./templates/**/*.{html,js}", "./home/templates/**/*.{html,js}"],
  theme: {
    extend: {
      backgroundImage: {
        "background-pattern": "url('/static/img/background.svg')",
        "hero-background": "url('/static/img/hero-texture-33-4.jpg')",
      },
      colors: {
        primary: "#602627"
      },
    },
  },
  plugins: [],
};
