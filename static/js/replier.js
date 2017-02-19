$(document).ready(function () {
    $(".comment-reply-btn").click(function (event) {
        event.preventDefault();
        const replyBlock = $(this).parent().next(".comment-reply").show();
    });
});