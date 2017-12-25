var modal = document.getElementById("AddModal");
var btn = document.getElementById("add");
var span = document.getElementsByClassName("close")[0];


span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function () {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

btn.onclick = function () {
    modal.style.display = "block";
}

// $(".right-corder-container-button").hover(function() {
//     $(".long-text").addClass("show-long-text");
// }, function () {
//     $(".long-text").removeClass("show-long-text");
// });