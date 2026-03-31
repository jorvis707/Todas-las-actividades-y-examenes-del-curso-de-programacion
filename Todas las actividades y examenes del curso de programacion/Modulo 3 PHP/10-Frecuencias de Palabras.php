<?php
$palabras = ["musica", "codigo", "musica", "pc", "musica", "codigo"];
$frecuencias = [];

foreach ($palabras as $p) {
    if (isset($frecuencias[$p])) {
        $frecuencias[$p]++;
    } else {
        $frecuencias[$p] = 1;
    }
}

echo "Frecuencia de palabras: \n";
foreach ($frecuencias as $palabra => $conteo) {
    echo "$palabra: $conteo veces \n";
}
?>