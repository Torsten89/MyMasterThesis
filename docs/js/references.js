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
    },
    {
        "id":"DavidisKochbuchDTA",
        "authors":"Deutsches Textarchiv (A)",
        "year":"2008",
        "title":"Davidis, Henriette: Praktisches Kochbuch für die gewöhnliche und feinere Küche. 4. Aufl. Bielefeld, 1849 - Digitalisiert vom Deutschem Text Archiv",
        "location":"Berlin-Brandenburgische Akademie der Wissenschaften",
        "url":"http://www.deutschestextarchiv.de/book/show/davidis_kochbuch_1849",
        "date":"2017-01.06"
    },
    {
        "id":"ZielDTA",
        "authors":"Deutsches Textarchiv (B)",
        "year":"2017",
        "title":"DTA - Projektüberblick",
        "location":"Berlin-Brandenburgische Akademie der Wissenschaften",
        "url":"http://www.deutschestextarchiv.de/doku/ueberblick",
        "date":"2017-01.07"
    },
    {
        "id":"TEI",
        "authors":"TEI-Konsortium (A)",
        "year":"2017",
        "title":"TEI-Konsortium",
        "location":"University of Virginia Library, Charlottesville VA 22904-4114, USA",
        "url":"http://www.tei-c.org/index.xml"
    },
    {
        "id":"TEIP5",
        "authors":"TEI-Konsortium (B)",
        "year":"2017",
        "title":"TEI P5: Guidelines for Electronic Text Encoding and Interchange. Version 3.1.0.",
        "url":"http://www.tei-c.org/Guidelines/P5/",
        "date":"2017-01-07"
    },
    {
        "id":"ChefkochPfannekuchen",
        "authors":"06onkel von Chefkoch.de",
        "year":"2017",
        "title":"Rezept für Pfannekuchen",
        "url":"http://www.chefkoch.de/rezepte/363861121870267/Pfannekuchen.html",
        "date":"2017-01-07"
    },
    {
        "id":"CRFNYT",
        "authors":"Greene",
        "year":"2015",
        "title":"Extracting Structured Data From Recipes Using Conditional Random Fields",
        "in":"The New York Times",
        "url":"https://open.blogs.nytimes.com/2015/04/09/extracting-structured-data-from-recipes-using-conditional-random-fields/?_r=1",
        "date":"2017-01-08"
    }
].sort(function(a,b) {
   return a.authors > b.authors;
});


$("span[cite]").each(function() {
    var stem = $(this)[0].hasAttribute("stem") ? $(this).attr("stem") : "";
    var supplement = $(this)[0].hasAttribute("supplement") ? $(this).attr("supplement") : "";
    $(this).html(cite($(this).attr("cite"), stem, supplement));
});



function cite(id, stem, supplement) {
    for(var i=0; i<references.length; i++) {
       if(references[i].id == id) {
           return ref2Cite(references[i], stem, supplement);
       }
    }
}

function ref2Cite(ref, stem, supplement){
    var href = "Quellen.html#" + ref.id;
    return "<a href='" + href + "' title='" + ref.title + "'> \
                (" + stem + getAuthorRepresentationOfRef(ref) + ", " + ref.year + supplement + ") \
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
    var authors = ref.authors.split(", ");
    return (authors.length > 2) ? authors[0]+" et al." : ref.authors;
}