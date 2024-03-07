function setTimeZone(e) {
  let dateEls = document.getElementsByClassName("local-date");
  let timeEls = document.getElementsByClassName("local-time");
  for (const el of dateEls) {
    const unixDate = dayjs(Number(el.dataset.date) * 1000);
    el.textContent = unixDate.format("MMM D, YYYY");
  }
  for (const el of timeEls) {
    const unixDate = dayjs(Number(el.dataset.time) * 1000);
    el.textContent = unixDate.format("h:mm a");
  }
}

window.addEventListener("load", setTimeZone);

window.addEventListener("htmx:oobAfterSwap", setTimeZone);

