<?php
$valores = [45, 12, 89, 3, 27, 56];
$max = $valores[0];
$min = $valores[0];

foreach ($valores as $v) {
    if ($v > $max) {
        $max = $v;
    }
    if ($v < $min) {
        $min = $v;
    }
}

echo "El numero mayor es: $max \n";
echo "El numero menor es: $min \n";
?>