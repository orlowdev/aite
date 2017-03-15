'use strict';

angular.module('prep').
    config(function($locationProvider, $routeProvider){
    	$locationProvider.html5Mode({
    		enabled:true
    	})
    	$routeProvider.
    		when("/", {
    			template: "<blog-list></blog-list>"
    		}).
    		when("/about", {
    			templateUrl: "/api/templates/about.html"
    		}).
            when("/blog", {
                template: "<blog-list></blog-list>"
            }).
    		when("/blog/:id", {
    			template: "<blog-detail></blog-detail>"
    		}).
    		otherwise({
    			template: "Not found"
    		})

    });