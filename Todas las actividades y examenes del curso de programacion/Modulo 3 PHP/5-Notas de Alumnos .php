<?php
$alumnos = [
    "Jose" => 95,
    "Carlos" => 58,
    "Jonathan" => 75,
    "Maria" => 40
];

foreach ($alumnos as $nombre => $nota) {
    $estado = ($nota >= 60) ? "APROBADO" : "REPROBADO";
    echo "Alumno: $nombre - Nota: $nota - Estado: $estado \n";
}
?>