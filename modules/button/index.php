<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/button/button.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Enter button color and text</input>

    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>