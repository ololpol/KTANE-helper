function updateText() {

    // Read data from webpage
    p1 = document.getElementById("In1").value;
    p2 = document.getElementById("In2").value;
    p3 = document.getElementById("In3").value;
    p4 = document.getElementById("In4").value;
    p5 = document.getElementById("In5").value;
    p6 = document.getElementById("In6").value;
    p7 = document.getElementById("In7").value;

    p2 = p2+"-"+p3+"-"+p4+"-"+p5+"-"+p6+"-"+p7;

    var raw = JSON.stringify({
    "p1": p1,
    "p2": p2
    });

    sendRequest(raw)
    .then(result => document.getElementById("ReturnBox").innerHTML = result.value)
    .catch(error => console.log('error', error));
}