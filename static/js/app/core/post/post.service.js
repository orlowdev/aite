'use strict';

angular.module('core.post').
factory('Post', function ($resource) {

    var url = '/api/posts/:slug/';

    return $resource(url, {}, {
        query: {
            method: "GET",
            params: {},
            isArray: true,
            cache: false,
            transformResponse: function (data, headersGetter, status) {
                return angular.fromJson(data).results;
            }
        },
        get: {
            method: "GET",
            params: {"slug": "@slug"},
            isArray: false,
            cache: false,
        }
    })
});