function createElement(type, attributes, inner) {
    var el = document.createElement(type);
    if (attributes) {
        for (var key in attributes) {
            el.setAttribute(key, attributes[key]);
        }
    }
    if (inner) el.innerHTML = inner;
    return el;
}