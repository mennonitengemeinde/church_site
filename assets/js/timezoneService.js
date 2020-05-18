window.addEventListener("load", function (e) {
    let dateEls = document.getElementsByClassName("local-date");
    let timeEls = document.getElementsByClassName("local-time");
    for (const el of dateEls) {
        const unixDate = moment.unix(Number(el.dataset.date));
        el.innerHTML = el.innerHTML + unixDate.format("MMM Do, YYYY");
    }
    for (const el of timeEls) {
        const unixDate = moment.unix(Number(el.dataset.time));
        el.innerHTML = el.innerHTML + unixDate.format("h:mm a");
    }
});