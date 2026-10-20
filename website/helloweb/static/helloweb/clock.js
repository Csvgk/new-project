setInterval(function () {
        var now = new Date();
        document.getElementById("clock").textContent = now.toLocaleTimeString("uk-UA");
    }, 1000);