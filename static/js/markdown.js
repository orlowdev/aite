$(document).ready(function () {
    let $previewContent = $("#preview-content");
    let $previewTitle = $("#preview-title");

    $(".content-markdown").each(function () {
        let content = $(this).text();
        let markedContent = marked(content);
        $(this).html(markedContent);
    });
    $(".post-detail-content img").each(function () {
        $(this).addClass("img-responsive");
    });

    let titleInput = $("#id_title");

    let contentInput = $("#id_content");

    let contentSetter = value => {
        let markedContent = marked(value);
        $previewContent.html(markedContent);
        $previewContent.find("img").each(function () {
            $(this).addClass("img-responsive");
        })
    };

    let titleSetter = value => {
        $previewTitle.text(value);
    };

    titleSetter(titleInput.val());
    titleInput.keyup(function () {
        let newContent = $(this).val();
        titleSetter(newContent);
    });

    contentSetter(contentInput.val());
    contentInput.keyup(function () {
        let newContent = $(this).val();
        contentSetter(newContent);
    })
});