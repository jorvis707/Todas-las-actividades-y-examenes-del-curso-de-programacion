<?php
$rol = "admin";

$acceso = ($rol == "admin") ? "Acceso Total" : 
          (($rol == "editor") ? "Acceso de Edicion" : 
          "Acceso de Invitado");

echo $acceso;
?>