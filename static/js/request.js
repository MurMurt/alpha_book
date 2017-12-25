function request(url, type, body, headers) {
    return new Promise(function (resolve, reject) {
        if (!headers) {
            headers = {};
        }
        headers['X-CSRFToken'] = getCsrf();
        var fetchObj = {
            method: type,
            headers: headers,
            credentials: 'include'
        };
        if (body) {
            fetchObj.body = JSON.stringify(body);
        }
        var result = {};
        fetch(url, fetchObj).then(function (res) {
            result = {
                redirected: res.redirected,
                url: res.url,
                status: res.status
            };
            if (res.redirected) {
                return {};
            }
            return res.json();
        }).then(function (json) {
            result.json = json;
            resolve(result);
        }).catch(function (err) {
            reject(err);
        });
    });
}