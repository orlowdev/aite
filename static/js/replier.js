$(document).ready(function () {
    $(".comment-reply-btn").on("click", function (event) {
        event.preventDefault();
        $(this).parent().next(".comment-reply").fadeToggle();
        if (replyBlock.show()) {}
    });
});