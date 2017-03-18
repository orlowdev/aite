'use strict';

angular.module('core.comment').
directive('commentReplyThread', function (Comment) {
   return {
      restrict: "E",
      scope: {
         comment: '=comment',
      },
      template: "<div ng-show='replies'><div class='row' style='margin-top: 20px;' ng-repeat='reply in replies'><div class='col-md-12'><div class='panel panel-default'><div class='panel-body'>{{ reply.content }}<br/>{{ user }} | <a href='#'><i class='glyphicon glyphicon-remove'></i></a></div></div><div></div></div>" +
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