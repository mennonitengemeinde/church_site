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
 * @param {string} serverTimezone
 */
function setTimezone(serverTimezone) {
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    if (serverTimezone !== timezone) {
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
                    if (data.reload === true) {
                        window.location.reload();
                    }
                } else {
                    console.error(data);
                }
            })
            .catch((error) => console.error('Error:', error));
    }
}
