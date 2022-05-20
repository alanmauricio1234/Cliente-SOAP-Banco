¡¡¡Hola!!!
Este proyecto es realizado en Python, específicamente en Django, y es un cliente
soap que consume un servicio web del proyecto banco_soap.
En esta aplicación se realiza una especie de cajero automático (ATM) de un banco.
Donde las funciones son las siguientes:
-> Ingresar el número de tarjeta
    - Se verifica el número de tarjeta
    - Se verifica que la fecha de vencimiento de la tarjeta
    - Se verifica que la tarjtea no esté bloqueada
    - Se realiza una simulación de vericación del chip de la tarjeta
-> Ingresar el nip
    - Se realiza la verificación de nip y se le dan al cliente 3 intentos
    en caso de revesar los intentos se bloquea la tarjeta.
-> Realizar el retiro de efectivo
    - Se verifica que la cantidad a retirar sea menor que el límite establecido
    - Se verifica que la cantidad sea menor o igual al saldo
    
    <<Requerimientos del Proyecto>>>
Los requerimientos necesarios para ejecutar la aplicación web los encuentra en el
archivo requirements.txt, para instarlos solo tiene que ejecutar el siguiente comando
    pip install -r requirements.txt
Con esto comenzará la descarga de todas las dependencias para el funcionamiento del
proyecto.

    Nota importante: Se recomienda crear un entorno virtual donde pueda descargar
    todas las dependencias del proyecto. Para la creación de un entorno virtual en
    python se tienen que ejecutar los siguientes comandos:
        pip install virtualenv
        python -m venv nom_carpeta

    <<Forma de Ejecutarlo>>
La manera de ejecutar un proyecto en Django es la siguiente:
    python manage.py runserver
Por defecto Django corre el servidor en el puerto 8000, sin embargo para poder
ejecutar de manera efectiva el proyecto completo, es decir, el cliente y el 
servicio web tenemos que considerar que el servicio se debe de ejecutar primero
y se ejecuta en el puerto por defecto. Entonces, el cliente debe de ejecutarse
en otro puerto que no se encuentre ocupado. En mi caso el puerto 4000. Para
indicarle eso a Django lo que hacemos es lo siguiente:
    python manage.py runserver 4000
Con esto le indicamos a Django que el servidor lo ejecute en el puerto 4000 y 
así solucionamos los conflictos de puertos para correr el servidor.

