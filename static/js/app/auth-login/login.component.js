'use strict';

angular.module('login').
component('login', {
    templateUrl: '/api/templates/login.html',
    controller: function ($http, $location, $routeParams, $rootScope, $scope) {
        var loginUrl = '/api/auth/token/';
        $scope.user = {
        };

        $scope.logUserIn = function (user) {

            var requestConfig = {
                method: "POST",
                url: loginUrl,
                data: {
                    username: user.username,
                    password: user.password,
                },
                headers: {}
            };

            var requestAction = $http(requestConfig);

            requestAction.then(
                // Success callback
                function(response_data, response_status, response_headers, response_config) {
                    console.log(response_data)
                },
                // Error callback
                function(error_data, error_status, error_headers, error_config) {
                    console.log(error_data)
                }
            );
        };
    }
});