
# Proyecto en Django (Modelo Predictivo)
## Descripción

Guía de documentacion de un proyecto de Django. ( Django:***4.2.5*** y python:***3.11.5***)


## Creacion del proyecto

1. Ejecutar el comando 

```
python -m django startproject <nombre del proyecto>
```

2. Crear las aplicaciones con:

```
django startapp <nombre de la aplicacion>
```

## Instalación

Para instalar Django, sigue estos pasos:
1. Instala python en el ordenador. A partir del link: https://www.python.org/. Selecciona la versión v3.11.5.

2. Instalar el ejecutable .exe y agregarlo a las variables de entorno PATH.
   
3. En una consola Bash ejecutar los siguientes comandos:

```
git init
git clone https://github.com/CR1B1/Modelo-Predictivo-Gestion-Incidencias.git
```
  *Si no en su defecto, bajar la carpeta y descomprimirla, luego abrir ese folder en VScode.*
   
4. Crea una terminal en VScode y crea un entorno virtual, con el comando:

```
python -m venv venv
```

5. Activa el entorno virtual:

```
venv/Scripts/activate
```

6. Instala todas las dependencias, con el siguiente comando:

```
pip install -r requirements.txt
``````

7. Ejecuta las migraciones con los siguientes comandos:

```
1. python manage.py makemigrations
2. python manage.py makemigrations authentication
3. python manage.py migrate
```

8. Ejecuta el servidor, con el siguiente comando:

```
python manage.py runserver
```

9. Para usar este proyecto, visita la siguiente dirección en tu navegador:

http://127.0.0.1:8000

## Dependencias

Este proyecto utiliza los siguientes paquetes:

```asgiref             3.7.2  
Django              4.2.5  
django-cors-headers 4.2.0  
pip                 23.2.1 
python-decouple     3.8    
setuptools          65.5.0 
sqlparse            0.4.4  
tzdata              2023.3
Unipath             1.1
whitenoise          6.5.0
```

## Configuración

La configuración de este proyecto se encuentra en el archivo `settings.py`.

## Modelos

Los modelos de este proyecto se encuentran en los archivos `models.py`.

## Vistas

Las vistas de este proyecto se encuentran en los archivos `views.py`.

## Plantillas

Las plantillas de este proyecto se encuentran en la carpeta `templates`.

# Estructura de carpetas:

├───authentication
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   │   ├───css
│   │   ├───img
│   │   ├───js
│   │   └───lib
│   │       ├───animate
│   │       ├───easing
│   │       ├───owlcarousel
│   │       │   └───assets
│   │       ├───waypoints
│   │       └───wow
│   ├───templates
│   │   ├───accounts
│   │   ├───home
│   │   ├───includes
│   │   └───layouts
│   └───__pycache__
├───core
│   └───__pycache__
├───nginx
├───public
│   ├───static
│   │   ├───assets
│   │   │   ├───css
│   │   │   ├───fonts
│   │   │   │   ├───flaticon
│   │   │   │   ├───fontawesome
│   │   │   │   ├───simple-line-icons
│   │   │   │   └───summernote
│   │   │   ├───img
│   │   │   │   ├───examples
│   │   │   │   ├───flags
│   │   │   │   └───productimg
│   │   │   ├───js
│   │   │   │   ├───core
│   │   │   │   └───plugin
│   │   │   │       ├───bootstrap-notify
│   │   │   │       ├───chart-circle
│   │   │   │       ├───chart.js
│   │   │   │       ├───datatables
│   │   │   │       ├───jquery-scrollbar
│   │   │   │       ├───jquery-ui-1.12.1.custom
│   │   │   │       ├───jquery-ui-touch-punch
│   │   │   │       ├───jquery.sparkline
│   │   │   │       ├───jqvmap
│   │   │   │       │   └───maps
│   │   │   │       │       └───continents
│   │   │   │       ├───sweetalert
│   │   │   │       └───webfont
│   │   │   └───sass
│   │   │       └───atlantis
│   │   │           ├───components
│   │   │           └───plugins
│   │   ├───css
│   │   ├───img
│   │   ├───js
│   │   ├───lib
│   │   │   ├───animate
│   │   │   ├───easing
│   │   │   ├───owlcarousel
│   │   │   │   └───assets
│   │   │   ├───waypoints
│   │   │   └───wow
│   │   └───scss
│   │       └───bootstrap
│   │           └───scss
│   │               ├───forms
│   │               ├───helpers
│   │               ├───mixins
│   │               ├───utilities
│   │               └───vendor
│   ├───templates
│   └───__pycache__
├───static
│   └───assets
│       ├───css
│       ├───fonts
│       │   ├───flaticon
│       │   ├───fontawesome
│       │   ├───simple-line-icons
│       │   └───summernote
│       ├───img
│       │   ├───examples
│       │   ├───flags
│       │   └───productimg
│       ├───js
│       │   ├───core
│       │   └───plugin
│       │       ├───bootstrap-notify
│       │       ├───chart-circle
│       │       ├───chart.js
│       │       ├───datatables
│       │       ├───jquery-scrollbar
│       │       ├───jquery-ui-1.12.1.custom
│       │       ├───jquery-ui-touch-punch
│       │       ├───jquery.sparkline
│       │       ├───jqvmap
│       │       │   └───maps
│       │       │       └───continents
│       │       ├───sweetalert
│       │       └───webfont
│       └───sass
│           └───atlantis
│               ├───components
│               └───plugins
├───staticfiles
└───uwsgi

# Rutas del proyecto:
 
****Administracion de superusuarios*:***
```
127.0.0.1:8000/admin/
```
****Index****:

```
127.0.0.1:8000
127.0.0.1:8000/index/page/
```

****Authenticacion*:***
```
127.0.0.1:8000/auth/login/
127.0.0.1:8000/auth/register/
127.0.0.1:8000/auth/logout/
```
**Vista publica:**

```
127.0.0.1:8000/auth/login/
127.0.0.1:8000/auth/register/
127.0.0.1:8000/auth/logout/
```

# Requerimientos:
- [X] Sistema de authentication (Inicio de sesion, Registro de usuarios y cerrar sesion)
- [x] Crear modelos y usuarios por tipo de rol (Administrador, Manager y Empleado)
- [ ] Integracion con PostgreSQL ***v16.0***
- [ ] Registro de incidencias en la base de datos.


## Ejecucion del docker:

```
 docker compose up
```

### Para correrlo en background

```
 docker compose up -d
```