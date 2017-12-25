// function AddCommentPopup() {
//     this.text = document.getElementById('add-text');
//     this.addModal = document.getElementById('AddModal');
//     this.addSubmit = document.getElementById('add-submit');
//     this.init();
// }
//
// AddCommentPopup.prototype.init = function () {
//     this.setSubmitListener();
// };
//
// AddCommentPopup.prototype.setSubmitListener = function () {
//     var _this = this;
//     this.addSubmit.addEventListener('click', function (e) {
//         request('/add-comment/', 'POST', {
//             text: _this.text.value
//         }).then(function (res) {
//             console.warn(res);
//             _this.addModal.style.removeProperty('display');
//         }).catch(function (err) {
//             // alert(err);
//         });
//     });
// };
