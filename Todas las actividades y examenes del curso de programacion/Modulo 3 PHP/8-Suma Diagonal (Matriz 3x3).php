<?php
$matriz = [
    [10, 5, 3],
    [2, 20, 8],
    [4, 7, 30]
];

$sumaDiagonal = 0;

for ($i = 0; $i < 3; $i++) {
    $sumaDiagonal += $matriz[$i][$i];
}

echo "La suma de la diagonal principal es: $sumaDiagonal \n";
?>