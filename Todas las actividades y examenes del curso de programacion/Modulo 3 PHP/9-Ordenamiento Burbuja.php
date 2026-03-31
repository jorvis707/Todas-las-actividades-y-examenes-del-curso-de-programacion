<?php
$datos = [64, 34, 25, 12, 22, 11, 90];
$n = count($datos);

for ($i = 0; $i < $n - 1; $i++) {
    for ($j = 0; $j < $n - $i - 1; $j++) {
        if ($datos[$j] > $datos[$j + 1]) {
            // Intercambio usando variable temporal
            $temp = $datos[$j];
            $datos[$j] = $datos[$j + 1];
            $datos[$j + 1] = $temp;
        }
    }
}

echo "Array ordenado: \n";
print_r($datos);
?>