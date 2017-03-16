'use strict';

angular.module('blogDetail').
	component('blogDetail', { 
		templateUrl: "/api/templates/blog-detail.html",
		controller: function(Post, $http, $location, $routeParams, $scope) {
			Post.get({"slug": $routeParams.slug}, function (data) {
                $scope.post = data;
            });
			// Post.query(function (data) {
			// 	$scope.notFound = true
			// 	$scope.comments = []
            //
			// 	angular.forEach(data, function (post) {
			// 		if (post.id == $routeParams.id) {
			// 			$scope.notFound = false
			// 			$scope.post = post
			// 			if (post.comments) {
			// 				$scope.comments = post.comments
			// 			}
			// 			resetReply()
			// 		}
			// 	})
			// })

			$scope.deleteComment = function(comment) {
				$scope.$apply($scope.comments.splice(comment, 1))
			};

			$scope.addReply = function() {
				console.log($scope.reply);
				$scope.comments.push($scope.reply);
				resetReply();
			};

			function resetReply() {
				$scope.reply = {
					"id": $scope.comments.length + 1,
					"text": "",
				}
			}

			if ($scope.notFound) {
				$location.path("/");
			}
		}
	});
