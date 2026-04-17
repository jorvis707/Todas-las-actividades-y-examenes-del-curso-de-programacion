let mes = "Octubre";

switch (mes) {
    case "Diciembre":
    case "Enero":
    case "Febrero":
        console.log("Invierno");
        break;
    case "Marzo":
    case "Abril":
    case "Mayo":
        console.log("Primavera");
        break;
    case "Junio":
    case "Julio":
    case "Agosto":
        console.log("Verano");
        break;
    case "Septiembre":
    case "Octubre":
    case "Noviembre":
        console.log("Otoño");
        break;
    default:
        console.log("Mes no valido");
}