'use strict';

angular.module('core.comment').
directive('commentReplyThread', function (Comment) {
   return {
      restrict: "E",
      scope: {
         comment: '=comment',
      },
      template: "<ul ng-show='replies'><li ng-repeat='reply in replies'>{{ reply.content }}</li></ul>" +
      "<div ng-show='!replies' class='center-block'><img ng-src='/static/img/ring.gif' class='img-responsive'/></div>",
      link: function (scope, element, attr) {
         if (scope.comment && scope.comment.id) {
            Comment.get({
               id: scope.comment.id,
            }, function (success) {
               scope.replies = success.replies
            })
         }
      },
   }
});