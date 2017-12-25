function BooksList(node) {
    this.node = node;
    this.limit = 6;
    this.offset = 0;
    this.canLoadMore = true;
    this._init();
}

BooksList.prototype.incrementOffset = function () {
    this.offset += this.limit;
};

BooksList.prototype._init = function () {
    this.getBooks();
    this.initScrollListener();
};

BooksList.prototype.getBooks = function () {
    var _this = this;
    request('/get-books/' + '?limit=' + this.limit + '&offset=' + this.offset, 'GET').then(function (res) {
        if (res.status !== 200) {
            return;
        }
        _this.createCards(res.json);
    }).catch(function (err) {
        console.error(err);
    });
};

BooksList.prototype.createCards = function (data) {
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

BooksList.prototype.appendCard = function (card) {
    this.node.appendChild(card);
};

BooksList.prototype.createCard = function (data) {
    var mainContainer = createElement('div', {
        class: 'card col-sm-3'
    });
    var img = createElement('img', {
        class: 'card-img-top',
        src: '/' + data.img
    });
    var cardBody = createElement('div', {
        class: 'card-body'
    });
    var title = createElement('h3', {
        class: 'card-title'
    }, data.title);
    var author = createElement('p', {
        class: 'card-text'
    }, data.author);
    cardBody.appendChild(title);
    cardBody.appendChild(author);

    var hrefContainer = createElement('div', {
        class: 'card-body'
    });
    var a = createElement('a', {
        class: 'btn btn-info',
        id: 'more-btn',
        role: 'button',
        href: '/book/' + data.id
    }, 'More');
    hrefContainer.appendChild(a);

    mainContainer.appendChild(img);
    mainContainer.appendChild(cardBody);
    mainContainer.appendChild(hrefContainer);
    return mainContainer;
};

BooksList.prototype.initScrollListener = function () {
    var _this = this;
    window.onscroll = function () {
        var el = document.documentElement;
        if (el.scrollTop === el.scrollHeight - el.clientHeight && _this.canLoadMore) {
            _this.incrementOffset();
            _this.getBooks();
        }
    }
};
