# Descargar e instalar Python en Linux (Ubuntu)

1. Primero que todo descargamos el archivo "XZ compressed source tarball" de la verison de Python que sea de nuestra conveniencia. Link: https://www.python.org

2. Luego, accedemos a la carpeta de descargas con:
    
        cd Descargas

3. Ahora extraemos la carpeta de ese archivo con el siguiente comando:

        tar xf Python-3.x.x.tar.xz
    
    >Reemplaza las x con numeros de la version  

    >Si no recuerdas la version de Python que descargastes ejecuta el comando  "ls" ya que ahí te muestra todos los archivos en la carpeta de descargas

4. Después accedemos a esa carpeta con el comando:
        
        cd Python-3.x.x

5. Ahora verificamos que tengamos todos estos paquetes instalados:

    -  zlib1g-dev
    - libgdbm-dev
    - libnss3-dev
    - libssl-dev
    - libreadline-dev
    -  libffi-dev  
___
6. Si no tienes idea de si estos paquetes están instalados o si sabes si están instalados igualmente te recomiendo ejecutar el siguiente comando para verificar que todos estén correctamente instalados:

        sudo apt install wget make xz-utils build-essential zlib1g-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev

7. Luego de que todo esté correctamente instalado procedemos a escribir el siguiente comando para asegurarse de que tdas las dependencias esten instaladas

        ./configure --enable-optimizations"
    
    

8. Ahora escribimos el siguiente comando  para iniciar el proceso de compilación:

        make -j 8

    >Cambie el número 8 por la cantidad de procesadores que tenga su pc o laptop. Para hallar este número ejecute el comando "nproc"

9. Luego de que el proceso termine, pasamos a instalar con el siguiente comando para instalar los binarios de python en el sistema:

        sudo make altinstall

10. Ya con esto acabaria nuestra instalación. Para saber que todo está correctamente instalado escribimos el siguiente comando y nos deberia salir la version de python que instalamos:

        python3.x --version

>No escriba el tercer numero de la versión de Python, solo hasta el segundo.

>NOTA: No instale python con "make install", ya que así estaría sobreescribiendo a python3 con el intérprete que va a usar. Siempre use "make altinstall".

