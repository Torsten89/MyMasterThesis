// global var activeTab has to be set within the website before loading this script
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       $("#navbar").html(xhr.responseText);
       $("#"+activeTab).addClass("active");
    }
};
xhr.open("GET", "fragments/navbar.html", false);
xhr.send();