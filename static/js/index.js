window.onload = function () {
    // debugger;
    if (location.href.indexOf('books') !== -1) {
        window.bookList = new BooksList(document.getElementById('list-bitch-talala'));
        window.addBookPopup = new AddBookPopup();
    }
    else if (location.href.indexOf('book/') !== -1) {
        window.commentList = new CommentsList(document.getElementById('comments-list'));
        window.addCommentPopup = new AddCommentPopup();
    }


};