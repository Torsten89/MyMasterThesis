

$(window).on('resize', function(){
    drawLines();
});

// collapse first line of timeline
/*$("[fstLineToggle]").each(function() {
    var lineToToggle = $(this).attr("fstLineToggle");
    $("#"+lineToToggle).toggle(0);
});*/
drawLines();

//set onclick handler for fst line
$("[fstLineToggle]").each(function() {
    var lineToToggle = $(this).attr("fstLineToggle");
    if(lineToToggle == "") return;
    
    var toggledLine = $(this);
    $(this).click(function() {
        svg.empty();
        $("#"+lineToToggle).toggle(400, function() {
            toggledLine.toggleClass("active");
            drawLines();
        });
    });
});


// deactivate old active/in and collapse content when sndLine item clicked
var activeContent = "";
$("a.timelineItem").each(function() {
    $(this).click(function () {
        if(activeContent!= "") {
            $("a[href='"+activeContent+"']").attr("aria-expanded", "false");
            $("a.timelineItem").each(function() {
                $("#"+$(this).attr("href").replace("#", "")).removeClass("in");
            });
        }
        activeContent = $(this).attr("href");
    });
});


function drawLines() {
    svg = $("#mySvg");
    svgPosi = svg.offset();
    svgTop = svgPosi.top + $(window).scrollTop(); // + window-scroll because svg has position:absoulte (only on page-load)
    svgLeft = svgPosi.left;
    svg.empty();
    
    var fstLines = $("[fstLineToggle]");
    for(var i=0; i<fstLines.length-1; i++) {
        var ths = $(fstLines[i]);
        if(ths.hasClass("active")) {
            var lineToToggle = ths.attr("fstLineToggle");
            if (lineToToggle == "") continue;
            
            var sndLine = $("#"+lineToToggle).children("a");
            connectLines(ths, sndLine);
            connectMarkers(sndLine);
            connectLines(fstLines[i+1], sndLine[sndLine.length-1]);
        } else {
            connectLines(ths, fstLines[i+1]);
        }
    }
}

function connectLines(fstL, sndL) {
    var m1 = getCenterPoint(fstL);
    var m2 = getCenterPoint(sndL);
    svg.append(getLine(m1.x, m1.y, m2.x, m2.y)); 
}

function connectMarkers(timelineMarkers) {
    for(var i=0; i<timelineMarkers.length-1; i++) {
        var m1 = getCenterPoint(timelineMarkers[i]);
        var m2 = getCenterPoint(timelineMarkers[i+1]);
        svg.append(getLine(m1.x, m1.y, m2.x, m2.y));
    }
}

function getCenterPoint(elem) {
    elem = $(elem);
    var offset = elem.offset();
    var xPosi = offset.left + elem.outerWidth()/2;
    var yPosi = offset.top + elem.outerHeight()/2;
    return {x:xPosi, y:yPosi};
}

//parameters are absolute pixel values of screen (from jquerys offset)
function getLine(x1, y1, x2, y2) {
    var l = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    
    l.setAttribute('x1', x1-svgLeft);
    l.setAttribute('y1', y1-svgTop);
    var calculatedX2 = x2-svgLeft;
    var calculatedY2 = y2-svgTop;
    l.setAttribute('x2', calculatedX2);
    l.setAttribute('y2', calculatedY2);
    l.setAttribute('stroke', "black");
    l.setAttribute('stroke-width', "2px");
    
/*  
    handled through overflow:visible :D
    if(svg.width() < calculatedX2) svg.attr("width", calculatedX2);
    if(svg.height() < calculatedY2) svg.attr("height", calculatedY2);
*/
    
    return l;
}