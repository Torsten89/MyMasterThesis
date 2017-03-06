// collapse first line of timeline
/*$("[fstLineToggle]").each(function() {collapseFstLine($(this), 0) });*/
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


// set active dot and "load" content
var activeContent = "";
$(".sndLine").each(function() {
    //var dotClass = $(this).attr("dotClass");
    $(this).children(".timelineItem").each(function() {
        var id = $(this).attr("id");
        
        //set active dot
        $(this).click(function () {
            if($("#"+id +" span").hasClass("active")) {
                return // was already the active item
            }
            
            $(".sndLine .timelineDot").removeClass("active");
            $(this).children("span").addClass("active");
            
            // "load" content
            var contentId = "#" + id.replace("Item", "Content");
            var ths  = $(contentId);
            if(activeContent != "") {
                $(activeContent).toggle(400, function() { ths.toggle(400); });
            } else {
                ths.toggle(400);
            }
            activeContent = contentId;
        });
    });
});