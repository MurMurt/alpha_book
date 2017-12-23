var modal = document.getElementById("bookAddModal");
var btn = document.getElementById("addBookBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function () {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

$(".right-corder-container-button").hover(function() {
    $(".long-text").addClass("show-long-text");
}, function () {
    $(".long-text").removeClass("show-long-text");
});