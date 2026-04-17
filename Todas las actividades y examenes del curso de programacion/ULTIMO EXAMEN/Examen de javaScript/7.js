let lado1 = 10;
let lado2 = 10;
let lado3 = 10;

if (lado1 === lado2 && lado2 === lado3) {
    console.log("Triangulo Equilatero");
} else if (lado1 === lado2 || lado1 === lado3 || lado2 === lado3) {
    console.log("Triangulo Isosceles");
} else {
    console.log("Triangulo Escaleno");
}