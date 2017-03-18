'use strict';

angular.module('blogDetail').
component('blogDetail', {
   templateUrl: "/api/templates/blog-detail.html",
   controller: function(Comment, Post, $cookies, $http, $location, $routeParams, $scope) {
      var slug = $routeParams.slug;

      Post.get({"slug": slug}, function (data) {
         $scope.post = data;
         Comment.query({"slug": slug, "type": "post"}, function (data) {
            $scope.comments = data;
         });
      });

      $scope.newComment = {};
      $scope.reply = {};
      $scope.commentOrder = '-created_at';

      // TODO: FIX DELETION
      $scope.deleteComment = function(comment) {
         comment.$delete({
                  id: comment.id,
               },
               function (success) {
                  $scope.comments.splice(comment, 1)
               }, function (error) {
                  console.log(error.data)
               });
      };

      // TODO: FIX ADDING REPLIES
      $scope.addCommentReply = function (reply, parentComment) {
         Comment.create({
            content: reply.content,
            slug: slug,
            type: "post",
            parent_id: parentComment.id,

         }, function (successResponse) {
            parentComment.reply_count = parentComment.reply_count ? parentComment.reply_count += 1 : 1;
            reply.content = "";
         });
      };

      $scope.addComment = function() {
         Comment.create({
            content: $scope.newComment.content,
            slug: slug,
            type: "post",
         }, function (successResponse) {
            data.reply_count = 0;
            $scope.comments.unshift(successResponse);
            resetComment();
         }, function (errorResponse) {
            $scope.commentError = errorResponse.data;
         });
      };

      $scope.updateReply = function (comment) {
         comment.$update({
            id: comment.id,
            content: $scope.reply.content,
            slug: slug,
            type: "post",
         }, function (success) {
         }, function (error) {
            console.log(error.data);
         })
      };

      function resetComment() {
         $scope.newComment = {
            content: "",
         }
      }

      if ($scope.notFound) {
         $location.path("/");
      }
   }
});
