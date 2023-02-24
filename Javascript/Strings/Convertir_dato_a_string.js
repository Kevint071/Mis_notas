// Para convertir un tipo de dato a string se puede hacer lo siguiente:

var numero = 1;
var numString = toString(numero);

console.log(typeof numString); // string
console.log(typeof numero); // number

// Ahora la otra manera de convertir datos es con la clase String

var numString2 = String(numero);

console.log(typeof numString2); // string
console.log(typeof numero); // number