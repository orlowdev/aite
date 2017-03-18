'use strict';

angular.module('core.comment').
factory('Comment', function (LoginRequiredInterceptor, $cookies, $httpParamSerializer, $location, $resource) {
   var url = '/api/comments/:id/';
   var commentQuery = {
      url: url,
      method: "GET",
      params: {},
      isArray: true,
      cache: false,
      transformResponse: function (data, headersGetter, status) {
         return angular.fromJson(data).results;
      }
   };
   var commentCreate = {
      url: "/api/comments/create/",
      method: "POST",
      interceptor: {
         responseError: LoginRequiredInterceptor,
      },
   };
   var commentGet = {
      method: "GET",
      params: {"id": "@id"},
      isArray: false,
      cache: false,
   };
   var commentUpdate = {
      url: url,
      method: "PUT",
      params: {"id": "@id"},
      interceptor: {
         responseError: LoginRequiredInterceptor,
      },
   };
   var commentDelete = {
      url: url,
      method: "DELETE",
      params: {"id": "@id"},
      interceptor: {
         responseError: LoginRequiredInterceptor,
      },
   };

   var token = $cookies.get("token");

   if (token) {
      var authHeader = {"Authorization": "JWT " + token};
      commentCreate["headers"] = authHeader;
      commentDelete["headers"] = authHeader;
      commentUpdate["headers"] = authHeader;
   }

   return $resource(url, {}, {
      query: commentQuery,
      create: commentCreate,
      get: commentGet,
      update: commentUpdate,
      delete: commentDelete,
   })
});