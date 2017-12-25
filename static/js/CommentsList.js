function CommentsList(node) {
    this.node = node;
    this.limit = 3;
    this.offset = 0;
    this.canLoadMore = true;
    this._init();
}

CommentsList.prototype.incrementOffset = function () {
    this.offset += this.limit;
};

CommentsList.prototype._init = function () {
    this.getComments();
    this.initScrollListener();
};

CommentsList.prototype.getComments = function () {
    var url = window.location.href;
    var id = url.match(/book\/(\d+)/)[1];
    var _this = this;
    request('/get-comments/' + '?limit=' + this.limit + '&offset=' + this.offset + '&id=' + id , 'GET').then(function (res) {
        if (res.status !== 200) {
            return;
        }
        _this.createCards(res.json);
    }).catch(function (err) {
        console.error(err);
    });
};

CommentsList.prototype.createCards = function (data) {
    if (data.length === 0) {
        this.canLoadMore = false;
        return;
    }
    var _this = this;
    data.forEach(function (elData) {
        var card = _this.createCard(elData);
        _this.appendCard(card);
    });
};

CommentsList.prototype.appendCard = function (card) {
    this.node.appendChild(card);
};

CommentsList.prototype.createCard = function (data) {
    var mainContainer = createElement('div', {
        class: 'card-comment'
    });
    var username = createElement('h4', {
        class: 'card-header'
    }, 'User: ' + data.username);
    var cardBody = createElement('div', {
        class: 'card-block'
    });
    var rating = createElement('h4', {
        class: 'card-title'
    }, 'Rating: ' + data.rating);
    var text = createElement('p', {
        class: 'card-text'
    }, data.text);

    cardBody.appendChild(rating);
    cardBody.appendChild(text);
    mainContainer.appendChild(cardBody);
    mainContainer.appendChild(username);

    return mainContainer;
};

CommentsList.prototype.initScrollListener = function () {
    var _this = this;
    window.onscroll = function () {
        var el = document.documentElement;
        if (el.scrollTop === el.scrollHeight - el.clientHeight && _this.canLoadMore) {
            _this.incrementOffset();
            _this.getComments();
        }
    }
};
