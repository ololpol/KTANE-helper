function updateText() {

    // Read data from webpage
    p1 = document.getElementById("In1").value;
    p2 = document.getElementById("In2").value;
    p3 = document.getElementById("In3").value;
    p4 = document.getElementById("In4").value;
    p5 = document.getElementById("In5").value;

    var raw = JSON.stringify({
    "p1": p1,
    "p2": p2,
    "p3": p3,
    "p4": p4,
    "p5": p5
    });

    sendRequest(raw)
    .then(res => res.value)
    .then(result => document.getElementById("ReturnBox").innerHTML = result)
    .catch(error => console.log('error', error));
}