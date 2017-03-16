'use strict';

angular.module('navigation').
directive('navigation', function (Post, $cookies, $location) {
    return {
        restrict: "E",
        templateUrl: "/api/templates/navigation.html",
        link: function (scope, element, attr) {
            scope.items = Post.query();
            scope.selectItem = function($item, $model, $label) {
                $location.path("/blog/" + $item.id);
                scope.searchQuery = "";
            };

            scope.searchItem = function() {
                $location.path("/blog/").search("q", scope.searchQuery);
                scope.searchQuery = "";
            };

            scope.userLoggedIn = false;
            scope.$watch(function () {
                scope.userLoggedIn = !!$cookies.get("token");
            });


        }
    }
});