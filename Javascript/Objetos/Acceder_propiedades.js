const datos = {
    nombre: "Kevin",
    edad: 30,
    genero: "M"
}

// Para acceder a las propiedades o elementos de este objeto hay varias formas

// Forma 1

console.log(datos.nombre) // Kevin
console.log(datos.edad) // 30

// Forma 2

console.log(datos['nombre']) // Kevin
console.log(datos['edad']) // 30

// Tambien se aplican las mismas formas a funciones

// Forma 1

function verDatos(datosUsuario){
    return datosUsuario.nombre
}

console.log(verDatos(datos))

// Forma 2

function verDatos(datosUsuario){
    return datosUsuario.nombre
}

console.log(verDatos(datos))

// Forma 3

    // También se puede hacer obteniendo el elemento o la propiedad en el parámetro de la función

function verDatos({nombre, edad}){

    return [nombre, edad];
}

console.log(verDatos(datos));

// Forma 4

  // Esta forma es parecida a la forma 3

function verDatos(datosUsuario){
    const {nombre, edad} = datosUsuario;
    return [nombre, edad]
}

console.log(verDatos(datos))