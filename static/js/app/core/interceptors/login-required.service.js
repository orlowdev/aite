'use strict';

angular.
module('core.interceptors').
factory("LoginRequiredInterceptor", function ($cookies, $location) {
   return function (response) {
      console.log("working");
      if (response.status == 401) {
         var currentPath = $location.path();
         var entryPoint = "/login";

         if (currentPath == entryPoint) {
            $location.path(entryPoint)
         }

         $location.path(entryPoint).search("next", currentPath);
      }
   }
});