function updateText() {
    p1 = document.getElementById("In1").value;

    var raw = JSON.stringify({
        "p1": p1
    });
    sendRequest(raw)
    .then(result => document.getElementById("ReturnBox").innerHTML = result.value)
    .catch(error => console.log('error', error));
}