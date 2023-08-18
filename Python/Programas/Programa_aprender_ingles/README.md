<style>
  h1 {
    color: #e6490b;
  }
  h2 {
    color: #0077b5;
  }
  code {
    background-color: #222;
    color: #fffddd;
    padding: 2px 4px;
    border-radius: 4px;
  }
  p,
  ul,
  li {
    
    font-size: 16px;
  }
</style>

<h1>Cómo usar este programa con una base de datos para aprender vocabulario de inglés</h1>

<h2>1. Crea una cuenta en fl0</h2>
<p>Crea una cuenta gratuita en fl0 para obtener acceso a una base de datos PostgreSQL hosted.</p>

<h2>2. Crea una tabla</h2>
<p>Una vez tengas acceso a la base de datos, crea una tabla llamada palabras con los siguientes campos:</p>

<ul>
  <li>id: llave primaria autoincremental</li>
  <li>palabra: texto con la palabra en inglés</li>
  <li>traduccion: texto con la traducción al español</li>
</ul>

<p>Puedes crear la tabla ejecutando el siguiente SQL:</p>

<code>CREATE TABLE palabras (
id SERIAL PRIMARY KEY,
palabra TEXT,
traduccion TEXT
);</code>

<h2>3. Crea un archivo credenciales.py</h2>
<p>Crea un archivo llamado credenciales.py en la carpeta Programa_aprender_ingles con los datos de conexión a tu base de datos:</p>

<code>from psycopg2 import connect

conn = connect("postgres://fl0user:cGbsEdO3mL9u@ep-little-violet-60084371.ap-southeast-1.aws.neon.tech:5432/palabras?sslmode=require")</code>

<p>Reemplaza usuario, contraseña, host, puerto y db con los valores correspondientes a tu base de datos.</p>

<h2>4. Ejecuta el programa</h2>
<p>Finalmente, ejecuta el programa Aprender_palabras.py para interactuar con la base de datos. Podrás agregar palabras nuevas, estudiar las existentes, y más.</p>

<p>¡Y eso es todo! Sigue estos pasos para configurar una base de datos PostgreSQL para aprender vocabulario en inglés con este programa.</p>
