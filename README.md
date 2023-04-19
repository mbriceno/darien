El proyecto esta configurado para ser instalado localmente o haciendo uso de Vagrant, así mismo incluye los archivos Dockerfile y docker-compose.yml para ejecutar el proyecto con el gestor docker-compose.

Solución:
=========

#### Arquitectura:

- Se utilizó una estructura básica monolítica, Modelo-Vista-Template haciendo uso de las herramientas que el framework posee.
- Conexión a una base de datos Postgresql.
- Gestión básica de usuarios con el módulo Auth de Django.
- Se usaron módulos desarrollados para Django para la gestión de las políticas de seguridad de la aplicación:
    * `django-csp`: Implementar content security policicy básicas.
    * `django-permissions-policy`: Implementar permissions policy básicas.
- El proyecto se implementó en dos (2) módulos:
    * **commons**: para implementar modelos bases del proyecto, como Client
    * **credits**: para implementar los modelos relacionados al crédito, como Bank y Credit.

#### Estructura:

- Se usaron vistas basadas en clases que implementan las vistas genéricas de Django
- Dentro de cada módulo se cambió la estructura por defecto de Django para hacer una mejor separación de conceptos, para esto se crearon los directorios models y views, dentro de los cuales cada script implementa un modelo con su respectiva vista asociada, ejemplo:
    * **credits**:
        - models:
           - `__init__.py`
           - `bank.py`
           - `credit.py`
        - views:
           - `__init__.py`
           - `bank.py`
           - `credit.py`

#### Interfaz:

- Implementación básica con Bootstrap 4.x
- Inicio de sesión en la página principal
- Menú de navegación en la parte superior
- Los formularios se implementaron con `django-crispy-forms` para agregarle estilos bootstrap por defecto.

#### Test Unitarios:

- Se implementaron test unitarios para modelos y vistas de ambos modulos.




Configuración
=============

Linux/Ubuntu:
-------------

Instale el requiriment
```sh
python3 -m pip install -r requirements.txt
```

Database:

Instale la base de datos:

```sh
sudo apt-get install postgresql
```

Asegurese de tener instalado libpq-dev para el correcto funcionamiento del driver de postgresql en django

```sh
sudo apt-get install libpq-dev
```

Cree la base de datos y usuario que usara el proyecto:

```sh
$ sudo su - postgres
$ psql

CREATE DATABASE dariendb;
CREATE USER darien_user WITH ENCRYPTED PASSWORD '1q2w3e4r5t';
GRANT ALL PRIVILEGES ON DATABASE dariendb TO darien_user;
```

El proyecto cuenta con variables de entorno en el archivo .env, se debe cambiar el archivo de .env.example para que el proyecto tome las variables desde ese archivo:

```sh
$ cd darien/
$ mv darien/.env.example darien/.env
```

Aplicar migraciones:

```sh
$ python manage.py makemigrations commons
$ python manage.py makemigrations credits
$ python manage.py migrate
```

Cree el superusuario para el django admin:

```sh
$ python manage.py createsuperuser
email: pruebas@yopmail.com
user: pruebas
pass: 1q2w3e4r5t
```

Docker Compose:
---------------

Para levantar el proyecto con docker:

En el directorio del proyecto hacer:

```sh
# Para construir la imagen del proyecto
docker build .

# Para levantar el compose y aprovisionar con las 2 imagenes python y postgres
docker-compose up

# Luego en otro terminal se debe inicializar la db con las migraciones del proyecto
docker-compose exec web python manage.py migrate

# Finalmente crear el usuario para acceder a la aplicación
docker-compose exec web python manage.py createsuperuser

email: pruebas@yopmail.com
user: pruebas
pass: 1q2w3e4r5t
```

La interfaz del proyecto estará disponible en la URL: `http://localhost:8000`
