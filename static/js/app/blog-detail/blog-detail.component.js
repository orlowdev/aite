'use strict';

angular.module('blogDetail').
component('blogDetail', {
    templateUrl: "/api/templates/blog-detail.html",
    controller: function(Post, $cookies, $http, $location, $routeParams, $scope) {
        var slug = $routeParams.slug;

    	Post.get({"slug": slug}, function (data) {
            $scope.post = data;
            $scope.comments = data.comments;
        });

        $scope.deleteComment = function(comment) {
            $scope.$apply($scope.comments.splice(comment, 1))
        };

        $scope.addReply = function() {
        	var token = $cookies.get("token");

        	if (token) {
        		var request = {
					method: "POST",
					url: "http://127.0.0.1:8000/api/comments/create/?slug=" + slug + "&type=post",
					data: {
						content: $scope.reply.content,
					},
					headers: {
						authorization: "JWT " + token,
					},
				};

        		$http(request).then(
        		    function (response) {
                        $scope.comments.push($scope.reply);
                        resetReply();
                    }, function (response) {
                        console.log(response);
                    }
                );

				console.log($scope.reply);
				resetReply();
			} else {
        		console.log("no token");
			}


        };

        function resetReply() {
            $scope.reply = {
                id: $scope.comments.length + 1,
                content: "",
            }
        }

        if ($scope.notFound) {
            $location.path("/");
        }
    }
});
