window.addEventListener("load", function (e) {
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
});

/**
 * @param {string} timezone
 */
function setTimezone(timezone) {
    fetch('/set_timezone/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({timezone}),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error(data);
            }
        })
        .catch((error) => console.error('Error:', error));
}