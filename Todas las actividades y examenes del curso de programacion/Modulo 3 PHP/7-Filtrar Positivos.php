<?php
$mixto = [-10, 15, 0, 33, -5, 8, -2];
$positivos = [];

foreach ($mixto as $num) {
    if ($num > 0) {
        $positivos[] = $num;
    }
}

echo "Array de solo positivos: \n";
print_r($positivos);
?>