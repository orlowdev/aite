'use strict';

angular.module('login').
component('login', {
   templateUrl: '/api/templates/login.html',
   controller: function ($cookies, $http, $location, $routeParams, $rootScope, $scope) {
      var loginUrl = '/api/auth/token/';
      $scope.user = {};

      var tokenExists = $cookies.get("token");
      if (tokenExists) {
         $scope.loggedIn = true;
         $cookies.remove("token");
         $scope.user = {
            username: $cookies.get("username"),
         };
         window.location.reload();
      }

      $scope.logUserIn = function (user) {

         var requestConfig = {
            method: "POST",
            url: loginUrl,
            data: {
               username: user.username,
               password: user.password,
            },
            headers: {},
         };

         var requestAction = $http(requestConfig);

         requestAction.then(
               // Success callback
               function(response) {
                  console.log(response.data.token);
                  $cookies.put("token", response.data.token);
                  $cookies.put("username", user.username);

                  // TODO: Add flash message
                  $location.path("/");
                  window.location.reload();
               },
               // Error callback
               function(response) {
                  console.log(response);
               }
         );
      };
   }
});