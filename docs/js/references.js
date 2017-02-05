references = [
    {
        "id":"KDT",
        "authors":"Feldman, Dagan",
        "year":"1995",
        "title":"Knowledge Discovery in Textual Databases (KDT)",
        "in":"Proceedings of the First International Conference on Knowledge Discovery and Data Mining",
        "pages":"112-117",
        "publisher":"AAAI Press",
        "location":"Montreal, Kanada",
        "url":"http://dl.acm.org/citation.cfm?id=3001335.3001354"
    },
    {
        "id":"TextMining",
        "authors":"Hohto, Nürnberger, Paaß",
        "year":"2005",
        "title":"A brief survey of text mining",
        "in":"LDV Forum - GLDV Journal for Computational Linguistics and Language Technology"
    },
    {
        "id":"Schema.org",
        "authors":"Schema.org",
        "year":"2017",
        "title":"http://schema.org/docs/datamodel.html",
        "url":"http://schema.org/docs/datamodel.html",
        "date":"2017-01-05"
    },
    {
        "id":"DavidisKochbuch",
        "authors":"Davidis",
        "year":"1849",
        "title":"Praktisches Kochbuch für die gewöhnliche und feinere Küche, 4. vermehrte u. verbesserte Auflage ",
        "publisher":"Velhagen und Klasing",
        location:"Bielefeld"
    }
].sort(function(a,b) {
   return a.authors > b.authors;
});


var cites = $("span[cite]");
for(var i=0; i<cites.length; i++) {
    var attris = cites[i].attributes;
    var supplement = (attris.length > 1) ? attris[1].value : "";
    cites[i].innerHTML = cite(attris[0].value, supplement);
}


function cite(id, supplement) {
    for(var i=0; i<references.length; i++) {
       if(references[i].id == id) {
           return ref2Cite(references[i], supplement);
       }
    }
}

function ref2Cite(ref, supplement){
    var href = "Quellen.html#" + ref.id;
    return "<a href='" + href + "' title='" + ref.title + "'> \
                (" + getAuthorRepresentationOfRef(ref) + ", " + ref.year + supplement + ") \
            </a>";
}

function getBibliography() {
    //Sorted by author name!!!
    var result = "";
    for(var i=0; i<references.length; i++) {
        result += ref2Bib(references[i]);
    }
    return result;
}

function ref2Bib(ref) {
    var result = '<p id="' + ref.id + '" style="text-indent:-4em;padding-left:4em">';
    result += '<b>'+ref.authors+' (' + ref.year +'). </b>';
    result += '"' + ref.title + '". ';
    if(ref.hasOwnProperty("in")) {
        result += 'In: ' + ref.in + ". ";
    }
    if(ref.hasOwnProperty("pages")) {
        result += "S. " + ref.pages + ". ";
    }
    if(ref.hasOwnProperty("location")) {
        result += ref.location + ". ";
    }
    if(ref.hasOwnProperty("publisher")) {
        result += ref.publisher + ". ";
    }
    if(ref.hasOwnProperty("url")) {
        result += '<a href="' + ref.url + '">' + ref.url + '</a>. ';
    }
    if(ref.hasOwnProperty("date")) {
        result += "Abgerufen am " + ref.date + ". ";
    }
    return result + '</p>';
}

function getAuthorRepresentationOfRef(ref) {
    var authors = ref.authors.split(", ")
    return (authors.length > 2) ? authors[0]+" et al." : ref.authors;
}