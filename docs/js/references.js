references = [
    {
        "id":"KDT",
        "authors":"Feldman, Ronen and Dagan, Ido",
        "year":"1995",
        "title":"Knowledge Discovery in Textual Databases (KDT)",
        "in":"Proceedings of the First International Conference on Knowledge Discovery and Data Mining",
        "pages":"112-117",
        "publisher":"AAAI Press",
        "location":"Montreal , Kanada",
        "url":"http://dl.acm.org/citation.cfm?id=3001335.3001354"
    }
]

function cite(id) {
    for(var i=0; i<references.length; i++) {
       if(references[i].id == id) {
           return ref2Str(references[i]);
       }
    }
}

function ref2Str(ref){
    var authors = ref.authors.split(", ")
    var authorString = (authors.length > 2) ? authors[0]+" et al." : ref.authors;
    var year = ref.year;
    return "(" + authorString + ", " + year +")";
}