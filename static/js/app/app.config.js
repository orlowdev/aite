'use strict';

angular.module('prep').
    config(function($locationProvider, $resourceProvider, $routeProvider){
    	$locationProvider.html5Mode({
    		enabled:true
    	});

    	$resourceProvider.defaults.stripTrailingSlashes = false;

    	$routeProvider.
    		when("/", {
    			template: "<blog-list></blog-list>"
    		}).
            when("/login", {
                template: "<login></login>"
            }).
    		when("/about", {
    			templateUrl: "/api/templates/about.html"
    		}).
            when("/blog", {
                template: "<blog-list></blog-list>"
            }).
    		when("/blog/:slug", {
    			template: "<blog-detail></blog-detail>"
    		}).
    		otherwise({
    			template: "Not found"
    		})

    });