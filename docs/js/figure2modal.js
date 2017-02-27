/* 
    This JS collects all figures, who have a "myModal"-attribute and adds on modal to it,
    which opens the img (the value of the "myModal"-attribute) in big.
    
    If a "myModalTitle" is given, its caption will be the value of "myModalTitle" and otherwise the content of the figcaption-element.
    The caption is also taken for the "alt"-element of the img.
    
    NOTE: This script should be called before references.js for the case if in the caption is a "<span cite=...".
*/
var figIdCounter = 0;
$("[myModal]").each(function() {
    figIdCounter += 1;
    var id = "myFigureID" + figIdCounter;
    caption = $(this)[0].hasAttribute("myModalTitle") ? $(this).attr("myModalTitle") : $(this).children("figcaption").html();
    caption = caption.replace(/'/g, '"');
    
    var modal =' \
    <div class="modal fade" id="' + id + '" role="dialog"> \
        <div class="modal-dialog" style="width:100%;"> \
            <div class="modal-content"> \
                <div class="modal-header">  \
                    <button type="button" class="close" data-dismiss="modal">&times;</button> \
                    <h4 class="modal-title">' + caption + '</h4> \
                </div> \
                <div class="modal-body"> \
                    <figure> \
                        <img src="' + $(this).attr("myModal") + '" alt="' + caption.replace(/"/g, '&quot;') + '"/> \
                    </figure> \
                </div> \
            </div> \
        </div> \
    </div>';
    $(this).after(modal);
    
    if(caption.startsWith("g")) {
        console.log(modal);
    }

    connectModalWithElem($(this), id);
});

function connectModalWithElem(elem, id) {
    var modalElem;
    if (elem.get(0).tagName == "FIGURE") {
        modalElem = elem.children("img");
        modalElem.attr("alt", caption);
    } else {
        modalElem = elem;
    }
    
    modalElem.attr("data-toggle", "modal");
    modalElem.attr("data-target", "#"+id);
    modalElem.attr("style", "cursor:pointer;");
}
