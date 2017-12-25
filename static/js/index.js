window.onload = function () {
    // debugger;
    if (location.href.indexOf('book/') !== -1) {
        new CommentsList(document.getElementById('comments-list'));
    }
    if (location.href.indexOf('books') !== -1) {
        window.bookList = new CommentsList(document.getElementById('list-bitch-talala'));
        window.addBookPopup = new AddBookPopup();
    }

};