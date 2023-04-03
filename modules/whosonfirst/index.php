<!DOCTYPE html>
    <head>
        <script src="/KTANE-helper/modules/whosonfirst/whosonfirst.js"> </script>
        <script src="/js/funcs.js"> </script>
        <link rel="stylesheet" href="/components/components.css"> </link>
    </head>

   
    <body>
    <?php
    function genSelection($options, $id = '') {
        if ($id != '') {
            $id = "id=\"$id\"";
        }
        $out = "<select " . $id . ' >';
        $out .= "<option value=\"select an option\">select an option</option>\n";
        foreach ($options as $option) {
            $out .= "<option value=\"$option\">$option</option>\n";
        }
        $out .= '</select>';
        echo $out;

    }
    $display = ['YES', 'FIRST', 'DISPLAY', 'OKAY', 'SAYS', 'NOTHING',
    ' ', 'BLANK', 'NO', 'LED', 'LEAD', 'READ',
    'RED', 'REED', 'LEED', 'HOLD ON', 'YOU', 'YOU ARE',
    'YOUR', 'YOU\'RE', 'UR', 'THERE', 'THEY\'RE', 'THEIR',
    'THEY ARE', 'SEE', 'C', 'CEE'];
    $options = ['YES', 'OKAY', 'WHAT', 'MIDDLE', 'LEFT', 'PRESS', 'RIGHT', 'BLANK', 'READY', 'NO', 'FIRST', 'UHHH', 'NOTHING', 'WAIT',
    'YOU\'RE', 'NEXT', 'U', 'UR', 'HOLD', 'DONE', 'UH UH', 'WHAT?', 'UH HUH', 'YOU', 'LIKE', 'SURE', 'YOU ARE', 'YOUR'];

    genSelection($display, "In1");
    echo "<br>";
    genSelection($options, "In2");
    genSelection($options, "In3");
    echo "<br>";
    genSelection($options, "In4");
    genSelection($options, "In5");
    echo "<br>";
    genSelection($options, "In6");
    genSelection($options, "In7");
    echo "<br>";
    ?>
    <button onclick="updateText()"> Submit </button>
    <div id="ReturnBox"> Result will show here </div>

    <?php require "../../components/bottom.php"; ?>
    </body>