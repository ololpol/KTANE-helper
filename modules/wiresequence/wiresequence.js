function updateText() {

    // Read data from webpage
    p1 = document.getElementById("In1").value;
    p2 = document.getElementById("In2").value;
    if (p2 == "") { //load past wires from counter and empty it
        p2 = document.getElementById("counter").innerHTML.substring(16);
    } //update counter to be filled later
    document.getElementById("counter").innerHTML = "";
    

    var raw = JSON.stringify({
    "p1": p1,
    "p2": p2
    });

    sendRequest(raw)
    .then(result => document.getElementById("ReturnBox").innerHTML = result.value)
    .catch(error => console.log('error', error));
    
    parts = p2.split(/[a-z]/)
    

    red = 0;
    blue = 0;
    black = 0;
    parts = p1.split(" ");
    for (i = 0; i < parts.length; i++) {
        if (parts[i][0] == "r") {
            red += 1;
        }
        if (parts[i][0] == "u") {
            blue += 1;
        }
        if (parts[i][0] == "b") {
            black += 1;
        }
    }

    if (p2 != "") {
        parts = p2.split(/[a-z]/)
        red += parseInt(parts[1]);
        blue += parseInt(parts[2]);
        black += parseInt(parts[3]);
    }
   
    
    document.getElementById("counter").innerHTML = "Previous wires: "+"r"+red+"u"+blue+"b"+black
    
}