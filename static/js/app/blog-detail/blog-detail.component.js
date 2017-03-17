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

        $scope.addReply = function() {
            Comment.create({
                content: $scope.reply.content,
                slug: slug,
                type: "post",
            }, function (successResponse) {
                $scope.comments.unshift(successResponse);
                resetReply();
            }, function (errorResponse) {
                console.log(errorResponse.data);
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

        function resetReply() {
            $scope.reply = {
                content: "",
            }
        }

        if ($scope.notFound) {
            $location.path("/");
        }
    }
});
