async function sendRequest(data, dest="") {

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");


    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: data,
    redirect: 'follow'
    }; //hello there
    if (dest == "") {
        url = window.location.href;
        dest = url.split('/')[4];
    }
    return fetch("http://localhost:8000/api/" + dest, requestOptions)
    .then(response => response.text())
    .then(text => JSON.parse(text));
    
}

async function submitBot(){
    var b1 = document.getElementById("botIn1").value;
    var b2 = document.getElementById("botIn2").value;
    var b3 = document.getElementById("botIn3").value;
    var b4 = document.getElementById("botIn4").value;
    var b5 = document.getElementById("botIn5").value;

    var raw = JSON.stringify({
    "serial": b1,
    "batteries": b2,
    "labels": b3,
    "ports": b4,
    "strikes": b5
    });

    sendRequest(raw, "updateBomb")
    .then(result => document.getElementById("botReturn").innerHTML = result.value)
    .catch(error => console.log('error', error));
}