var request = new XMLHttpRequest();
var button = document.getElementById("button");
var content = document.getElementById("content");
var phrase = "";

function send_request(){
    phrase = "";
    request.open("GET", "phrase", true);
    request.send();
}

button.addEventListener("mousedown", function() {
    if (phrase) {
        content.innerHTML = phrase;
        send_request();
    }
});

request.addEventListener("load", function() {
    phrase = this.responseText;
});

send_request();
