function toggle() {
    var x = document.getElementById("links");
    if (x.className == "hidden") {
        x.className -= " hidden";
    } else {
        x.className = "hidden";
    }
}