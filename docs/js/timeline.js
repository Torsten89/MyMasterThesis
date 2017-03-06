// collapse first line of timeline
$("[fstLineToggle]").each(function() {
    var lineToToggle = "#" + $(this).attr("fstLineToggle");
    $(lineToToggle).toggle(0);
});
$("[fstLineToggle]").each(function() {
    var lineToToggle = "#" + $(this).attr("fstLineToggle");
    $(this).click(function() {
        $(lineToToggle).toggle(400);
    });
});


// set active/in dot and collapse content
var activeContent = "";
$(".sndLine").each(function() {
    $(this).children(".timelineItem").each(function() {
        var id = $(this).attr("id");
        
        //set active/in dot
        $(this).click(function () {
            console.log("hi")
            console.log(activeContent)
            if(activeContent!= "") {
                $("#"+activeContent).attr("aria-expanded", "false");
                console.log(activeContent.replace("Item", "Content"));
                $("#"+activeContent.replace("Item", "Content")).removeClass("in");
            }
            activeContent = id;
/*            // "load" content
            var contentId = "#" + id.replace("Item", "Content");
            console.log(contentId);
            var ths  = $(contentId);
            if(activeContent != "") {
                $(activeContent).toggle(400, function() { ths.toggle(400); });
            } else {
                ths.toggle(400);
            }
            activeContent = contentId;*/
        });
    });
});