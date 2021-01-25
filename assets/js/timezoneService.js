window.addEventListener("load", function (e) {
    let dateEls = document.getElementsByClassName("local-date");
    let timeEls = document.getElementsByClassName("local-time");
    for (const el of dateEls) {
        const unixDate = dayjs(Number(el.dataset.date) * 1000);
        el.innerHTML = el.innerHTML + unixDate.format("MMM D, YYYY");
    }
    for (const el of timeEls) {
        const unixDate = dayjs(Number(el.dataset.time) * 1000);
        el.innerHTML = el.innerHTML + unixDate.format("h:mm a");
    }
});