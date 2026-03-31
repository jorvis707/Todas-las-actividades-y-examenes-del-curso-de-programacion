<?php
$numeroSecreto = 24;
$intento = 1;
$adivinado = 0;

while ($adivinado != $numeroSecreto) {
    echo "Intento $intento: Probando con el numero $adivinado... \n";
    
    if ($adivinado == $numeroSecreto) {
        echo "¡Logrado! El numero era $numeroSecreto. \n";
    }
    
    $adivinado++;
    $intento++;
}
?>