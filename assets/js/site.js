navigator.serviceWorker.getRegistrations().then(function (registrations) {
    registrations.forEach(registration => registration.unregister().then(console.log));
});

if ('caches' in window) {
    caches.keys()
        .then(keyList => Promise.all(keyList.map(caches.delete)));
}
