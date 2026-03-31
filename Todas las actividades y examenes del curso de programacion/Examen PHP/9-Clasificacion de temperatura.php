<?php
$temperatura = 15;

if ($temperatura < 10) {
    echo "La temperatura es: Fria ❄️ \n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "La temperatura es: Templada\n";
} else {
    echo "La temperatura es: Calurosa\n";
}
?>