<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/compwires/compwires.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Enter light status</input>
    <br>
    <input id="In2"> Enter wire colors, separated by space</input>
    <br>
    <input id="In3"> Enter star status</input>
    <br>

    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>