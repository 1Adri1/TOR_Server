    
    <?php
    $code = escapeshellcmd('sudo python3 /home/pi/tor.py '.$_GET["tor"]);
    $ergebnis = shell_exec($code);
    echo $ergebnis
    ?>
