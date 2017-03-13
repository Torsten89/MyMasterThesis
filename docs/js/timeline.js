var svg = $("#mySvg");
var svgPosi;
var svgTop;
var svgLeft;
var fstLines = $("[fstLineToggle]");
var activeContent = "";

$(window).on('resize', function(){
    drawLines();
});

// expand all for test purpose
// $("[fstLineToggle]").each(function() { $("#"+$(this).attr("fstLineToggle")).toggle(0); });
drawLines();

//set onclick handler for fst line (expand/collapse and redraw)
$("[fstLineToggle]").each(function() {
    var lineToToggle = $(this).attr("fstLineToggle");
    if(lineToToggle == "") return; // last timeline item is not expandable
    
    var toggledLine = $(this);
    $(this).click(function() {
        svg.empty(); // otherwise sndLine slides out while lines are still at their old position - which is ugly
        $("#"+lineToToggle).toggle(400, function() {
            toggledLine.toggleClass("active");
            drawLines();
        });
    });
});


// deactivate old in (active) and collapse content when sndLine item clicked
$("a.timelineItem").each(function() {
    $(this).click(function () {
        if(activeContent !=  "") {
            $("a[href='"+activeContent+"']").attr("aria-expanded", "false");
            $("a.timelineItem").each(function() {
                $("#" + $(this).attr("href").replace("#", "") ).removeClass("in");
            });
        }
        activeContent = $(this).attr("href");
    });
});


function drawLines() {
    svg.empty();
    svgPosi = svg.offset();
    svgTop = svgPosi.top;
    svgLeft = svgPosi.left;
    
    for(var i=0; i<fstLines.length-1; i++) {
        var fstLine = $(fstLines[i]);
        if(fstLine.hasClass("active")) {
            var lineToToggle = fstLine.attr("fstLineToggle");
            if (lineToToggle == "") continue; // last item has no expandable -> there are no sndLines to draw
            
            var sndLine = $("#"+lineToToggle).children("a");
            connectLines(fstLine, sndLine[0]);
            connectMarkers(sndLine);
            connectLines(sndLine[sndLine.length-1], fstLines[i+1]);
        } else {
            connectLines(fstLine, fstLines[i+1]);
        }
    }
}

function connectLines(elem1, elem2) {
    var m1 = getCenterPoint(elem1);
    var m2 = getCenterPoint(elem2);
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

// parameters are absolute pixel values of screen (from jquerys offset)
// for correct resizing of the svg y2 has to be the lower/bigger-value than y1
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
    
    if(svg.width() < calculatedX2) svg.attr("width", calculatedX2);
    if(svg.height() < calculatedY2) svg.attr("height", calculatedY2);
    
    return l;
}