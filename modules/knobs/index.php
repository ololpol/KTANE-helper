<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/knobs/knobs.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>
    <body>
    <input id="In1"> Enter top row</input>
    <br>
    <input id="In2"> Enter bot row</input>
    <br>
    Note that since the knobs rotation can be deferred from the rightmost three lights on each row, the first three lights can be omitted. If only 3 lights are given per row it is then assumed to be the last three

    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>