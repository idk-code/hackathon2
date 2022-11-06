function toggle() {
    var x = document.getElementById("links");
    if (x.className == "responsive") {
        x.className -= " responsive";
    } else {
        x.className = "responsive";
    }
}

function toggleDetails() {
    var x = event.target.previousElementSibling
    if (x.className == "hideDetails") {
        x.className -= "hidden";
        event.target.textContent = "Hide Details";
    } else {
        x.className = "hideDetails";
        event.target.textContent = "More Details";
    }
}