<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/maze/maze.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Enter position of any square</input>
    <br>
    <input id="In2"> Enter star position</input>
    <br>
    <input id="In3"> Enter goal position</input>
    <br>

    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>