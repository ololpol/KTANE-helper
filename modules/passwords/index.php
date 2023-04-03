<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/passwords/passwords.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

    <body>
    <input id="In1"> Char 1</input>
    <input id="In2"> Char 2</input>
    <input id="In3"> Char 3</input>
    <input id="In4"> Char 4</input>
    <input id="In5"> Char 5</input>

    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>