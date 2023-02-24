import { Link } from "react-router-dom";

const listaMenu = [
  {
    id: 1,
    title: "Introduccion a Python ",
    content: (
      <ul className="menu-content">
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
      </ul>
    ),
  },
  {
    id: 2,
    title: "Diccionarios",
    content: (
      <ul className="menu-content">
        <li>
          <Link to="Definicion">Definición</Link>
        </li>
        <li>
          <a href="#">Manipulación de elementos en un diccionario</a>
        </li>
        <li>
          <a href="#">Método get</a>
        </li>
        <li>
          <a href="#">Método items</a>
        </li>
        <li>
          <a href="#">Método keys</a>
        </li>
        <li>
          <a href="#">Método values</a>
        </li>
        <li>
          <a href="#">Mostrar valor de una key</a>
        </li>
      </ul>
    ),
  },
  {
    id: 3,
    title: "Excepciones",
    content: (
      <ul className="menu-content">
        <li>
          <a href="#">Zero division error</a>
        </li>
      </ul>
    ),
  },
  {
    id: 4,
    title: "Funciones",
    content: (
      <ul className="menu-content">
        <li>
          <a href="#">Función anonima lambda</a>
        </li>
        <li>
          <a href="#">Función \b</a>
        </li>
        <li>
          <a href="#">Función id</a>
        </li>
        <li>
          <a href="#">Función print</a>
        </li>
        <li>
          <a href="#">Función return</a>
        </li>
        <li>
          <a href="#">Función round</a>
        </li>
        <li>
          <a href="#">Operador is</a>
        </li>
        <li>
          <a href="#">Operador not</a>
        </li>
        <li>
          <a href="#">Palabra clave assert</a>
        </li>
        <li>
          <a href="#">Palabra clave class</a>
        </li>
        <li>
          <a href="#">Palabra clave del</a>
        </li>
        <li>
          <a href="#">Palabra clave pass</a>
        </li>
        <li>
          <a href="#">Punto de entrada</a>
        </li>
      </ul>
    ),
  },
  {
    id: 5,
    title: "Listas",
    content: (
      <ul className="menu-content">
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
      </ul>
    ),
  },
  {
    id: 6,
    title: "Módulos",
    content: (
      <ul className="menu-content">
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
        <li>
          <a href="#">Contenido de la opción 1</a>
        </li>
      </ul>
    ),
  },
  
];

export default listaMenu;
