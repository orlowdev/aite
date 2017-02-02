$(document).ready(function () {
    $(".content-markdown").each(function () {
        let content = $(this).text();
        let markedContent = marked(content);
        $(this).html(markedContent);
    });
    $(".content-markdown img").each(function () {
        $(this).addClass("img-responsive");
    })
});