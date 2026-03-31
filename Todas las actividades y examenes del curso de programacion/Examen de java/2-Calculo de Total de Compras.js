const nombreProducto = "laptop 15.6 pulgadas";
let precio = 450.99;
let cantidadComprada = 2;

let subtotal = precio * cantidadComprada;
let impuesto = subtotal * 0.07;
let totalFinal = subtotal + impuesto;

console.log("Subtotal: $" + subtotal.toFixed(2));
console.log("Total final (con 7% de impuesto): $" + totalFinal.toFixed(2));