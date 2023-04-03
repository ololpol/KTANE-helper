function updateText() {

    // Read data from webpage
    p1 = document.getElementById("In1").value;
    p2 = document.getElementById("In2").value;
    

    if (p2 == "") { //load past presses from counter and empty it
        p2 = document.getElementById("counter").innerHTML.substring(16);
    }

    var raw = JSON.stringify({
    "p1": p1,
    "p2": p2
    });

    sendRequest(raw)
    .then(result => {
        document.getElementById("ReturnBox").innerHTML = result.value;
        
        parts = p2.split(" ");
        console.log(parts);
        console.log(p2);
        
        out = "Previous wires: ";
        for (i = 0; i < parts.length; i++) {
            out += parts[i]+ " "
            console.log("i")
        }
    
        out += result.value //update with new button press
        
        document.getElementById("counter").innerHTML = out;
    })
    .catch(error => console.log('error', error));


    
}