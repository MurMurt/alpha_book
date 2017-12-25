//TODO Изменить

function AddBookPopup() {
    this.title = document.getElementById('add-title');
    this.author = document.getElementById('add-author');
    this.year = document.getElementById('add-year');
    this.pages = document.getElementById('add-pages');
    this.imageFile = document.getElementById('add-image');
    this.imgPrev = document.getElementById('add-img-prev');
    this.addSubmit = document.getElementById('add-submit');
    this.addModal = document.getElementById('AddModal');
    this.imgPrev.classList.add('hidden');
    this.init();
}

AddBookPopup.prototype.init = function () {
    this.setListenersImg();
    this.setSubmitListener();
};

AddBookPopup.prototype.setSubmitListener = function () {
    var _this = this;
    this.addSubmit.addEventListener('click', function (e) {
        request('/add-book/', 'POST', {
            img: _this.imgResultData,
            title: _this.title.value,
            author: _this.author.value,
            year: _this.year.value,
            pages: _this.pages.value
        }).then(function (res) {
            console.warn(res);
            _this.addModal.style.removeProperty('display');
        }).catch(function (err) {
            alert(err);
        });
    });
};

AddBookPopup.prototype.setListenersImg = function () {
    var _this = this;
    this.imageFile.onchange = function (el) {
        var target = el.currentTarget;
        if (target.files && target.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                _this.imgPrev.setAttribute('src', e.target.result);
                _this.imgResultData = e.target.result;
                _this.imgPrev.classList.remove('hidden');
            };

            reader.readAsDataURL(target.files[0]);
        }
    }
};