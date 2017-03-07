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


// deactivate old active/in and collapse content
var activeContent = "";
$("a.timelineItem").each(function() {
    $(this).click(function () {
        if(activeContent!= "") {
            $("#"+activeContent).attr("aria-expanded", "false");
            $("a.timelineItem").each(function() {
                $("#"+$(this).attr("id").replace("Item", "Content")).removeClass("in");
            });
        }
        activeContent = $(this).attr("id");;
    });
});