window.onload = function () {
    if (location.href.indexOf('book') !== -1) {
        // if (1 === 1) {
        // new ServiceList(document.getElementById('list-bitch-talala'));
        // new AddCommentPopup();
    }
    if (location.href.indexOf('books') !== -1) {
        new BooksList(document.getElementById('list-bitch-talala'));
        new AddBookPopup();
    }
};