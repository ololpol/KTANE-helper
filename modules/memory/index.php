<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/memory/memory.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Enter displayed number, followed by the numbers on the bottom panels, left to right.</input>
    <br>
    <input id="In2"> Enter previous buttons pressed in format {position}{number}.
    Alternatively leave empty to use values from the counter</input>
    <br>

    <button onclick="updateText()"> Submit </button>
    <div id="counter">Previous presses: </div>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>