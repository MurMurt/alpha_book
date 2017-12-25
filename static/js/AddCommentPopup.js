function AddCommentPopup() {
    this.text = document.getElementById('add-text');
    this.rating = document.getElementById('add-rating');
    this.addModal = document.getElementById('AddModal');
    this.addSubmit = document.getElementById('add-submit-comment');
    this.init();
}

AddCommentPopup.prototype.init = function () {
    this.setSubmitListener();
};

AddCommentPopup.prototype.setSubmitListener = function () {
    var _this = this;
    var bookRating = document.getElementById('book-rating');
    var url = window.location.href;
    var id = url.match(/book\/(\d+)/)[1];
    this.addSubmit.addEventListener('click', function (e) {
        request('/add-comment/', 'POST', {
            text: _this.text.value,
            book_id: id,
            rating: _this.rating.value

        }).then(function (res) {
            console.warn(res);
            if (res.status === 200) {
                bookRating.innerHTML = 'Rating: ' + res.json.rating;
            } else {
                throw new Error(res.json.err);
            }
            _this.addModal.style.removeProperty('display');
            var card = window.commentList.createCard({
               username: res.json.username,
               rating: _this.rating.value,
               text: _this.text.value
            });
            window.commentList.node.insertBefore(card, window.commentList.node.children[0]);
        }).catch(function (err) {
            alert(err);
        });
    });
};
