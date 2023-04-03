function updateText() {

    // Read data from webpage
    p1 = document.getElementById("In1").value;
    p2 = document.getElementById("In2").value;
    p3 = document.getElementById("In3").value;

    var raw = JSON.stringify({
    "p1": p1,
    "p2": p2,
    "p3": p3
    });

    sendRequest(raw)
    .then(result => document.getElementById("ReturnBox").innerHTML = result.value)
    .catch(error => console.log('error', error));
}