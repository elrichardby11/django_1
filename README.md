# Menú básico Django 

Esto es un menú de django para el registro de usuarios

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clona el Repositorio

```bash
git clone https://github.com/elrichardby11/django_1.git
cd django_1
```

### 2. Crea y Activa el Entorno Virtual

Para mantener las dependencias del proyecto aisladas, se recomienda utilizar un entorno virtual de Python. Sigue estos pasos para crear y activar el entorno virtual:

#### En Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### En macOS y Linux

```bash
python3 -m venv .venv
source .\.venv/bin/activate
```

### 3. Instala las Dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Crea la Base de Datos

El siguiente comando creará la base de datos necesaria:

```bash
python manage.py migrate
```

### 5. Ejecuta el Proyecto

Ahora estás listo para ejecutar el proyecto. Dependiendo de cómo esté configurado, puedes iniciar la aplicación con:

```bash
python manage.py runserver
```

## Demo
![image](https://github.com/elrichardby11/django_1/assets/76932746/52426910-7d6f-49ac-9007-bae37fc231c4)

