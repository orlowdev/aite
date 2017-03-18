'use strict';

angular.module('post').
	factory('Post', function ($resource) {
		var url = '/json/posts.json'
		return $resource(url, {}, {
			query: {
				method: "GET",
				params: {},
				isArray: true,
				cache: false,
				// transformResponse
				// interceptors
			},
			get: {
				method: "GET",
				params: {},
				isArray: true,
				cache: false,
			}
		})
	});