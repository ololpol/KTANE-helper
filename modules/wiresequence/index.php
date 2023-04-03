<!DOCTYPE html>
    <head>
        <script src="modules/wiresequence.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Enter wires in format {color}{destination}</input>
    <br>
    <input id="In2"> Enter previous wires in format {#red}{#blue}{#black}.
     Alternatively leave empty to use previous counts from the counter</input>
    <br>

    <button onclick="updateText()"> Submit </button>
    <div id="counter">Previous wires: </div>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>