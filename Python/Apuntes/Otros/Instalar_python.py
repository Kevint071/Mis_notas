# Primero que todo descargamos el archivo "XZ compressed source tarball" de la verison de Python que sea de nuestra conveniencia

# Luego, accedemos a la carpeta de descargas con "cd Descargas"

# Ahora extraemos la carpeta de ese archivo con el comando "tar xf Python-3.x.x.tar.xz" (Reemplaza las x con numeros de la version)

# Después accedemos a esa carpeta con el comando "cd Python-3.x.x"

# Ahora verificamos que tengamos todos estos paquetes instalados:

#  -  zlib1g-dev
#  - libgdbm-dev
#  - libnss3-dev
#  - libssl-dev
#  - libreadline-dev
#  -  libffi-dev

# Si no tienes idea de si estos paquetes están instalados o si sabes si están instalados igualmente te recomiendo ejecutar el siguiente comando para verificar que todos estén correctamente instalados:

# sudo apt install wget make xz-utils build-essential zlib1g-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

# Luego de que todo esté correctamente instalado procedemos a escribir el comando "./configure --enable-optimizations" para asegurarse de que tdas las dependencias esten instaladas

# Ahora escribimos el comando "make -j 8" para iniciar el proceso de compilación

# Cambie el número 8 por la cantidad de procesadores que tenga su pc o laptop. Para hallar este número ejecute el comando "nproc"

# Luego de que termine , pasamos a instalar con el comando "sudo make altinstall" para instalar los binarios de python en el sistema

# Ya con esto acabaria nuestra instalación. Para saber que todo está correctamente instalado escribirmos el comando "python3 --version" y nos deberia salir la version de python que instalamos

#NOTA: No instale python con "make install", ya que así estaría sobreescribiendo a python3 con el intérprete que va a usar. Siempre use "make altinstall"

