# Página Gimnasio

Aplicación web en Django para gestión de gimnasio, venta de planes, administración de usuarios y creación/seguimiento de rutinas de ejercicio.

## Tecnologías

- Python
- Django 6.0.3
- SQLite
- Django Allauth para autenticación y login social con Google
- HTML/CSS para templates y estilos

## Estructura principal

- `config/`: configuración del proyecto Django
- `gimnasio/`: app principal con vistas públicas y panel de administración
- `rutinas/`: app para creación, edición y seguimiento de rutinas y sesiones de entrenamiento
- `usuarios/`: app de autenticación y gestión de sesión personalizada
- `clases/`: app auxiliar para clases del gimnasio
- `templates/`: vistas HTML
- `static/`: archivos CSS e imágenes
- `media/`: archivos subidos como imágenes/videos de ejercicios

## Requisitos

- Python 3.11
- Virtualenv (recomendado)

## Instalación

1. Clona el repositorio o copia el proyecto a tu máquina.
2. Navega al directorio del proyecto:

```powershell
cd "c:\Users\crist\OneDrive\Documentos\Pagina-Gimnasio"
```

3. Crea y activa un entorno virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

4. Instala dependencias:

```powershell
pip install -r requirements.txt
```

5. Aplica migraciones:

```powershell
django-admin migrate
```

6. Crea un superusuario para acceder al admin:

```powershell
django-admin createsuperuser
```

## Ejecución

Inicia el servidor de desarrollo:

```powershell
django-admin runserver
```

Luego abre en el navegador:

```
http://127.0.0.1:8000/
```

## Rutas principales

- `/` : página de presentación
- `/planes/` : listados de planes disponibles
- `/sobreNosotros/` : página sobre el gimnasio
- `/galeria/` : galería de imágenes
- `/comprar/<id_plan>/` : comprar un plan
- `/inicio/` : inicio de sesión o página principal después de login
- `/usuarios/login/` : login de usuario
- `/usuarios/logout/` : cerrar sesión
- `/rutinas/` : listado de rutinas
- `/rutinas/crear/` : crear rutina
- `/rutinas/<pk>/` : detalle de rutina
- `/rutinas/<pk>/editar/` : editar rutina
- `/rutinas/<pk>/eliminar/` : eliminar rutina
- `/rutinas/<pk>/iniciar/` : iniciar sesión de entrenamiento
- `/rutinas/sesion/<pk>/` : ejecutar rutina de entrenamiento
- `/rutinas/sesion/<pk>/finalizar/` : finalizar sesión
- `/rutinas/historial/` : historial de sesiones

## Configuración adicional

- `AUTH_USER_MODEL = 'usuarios.Usuario'`
- `LOGIN_REDIRECT_URL = '/planes/'`
- `LOGOUT_REDIRECT_URL = '/'`
- `ACCOUNT_LOGOUT_ON_GET = True`
- `SOCIALACCOUNT_PROVIDERS` configurado para Google
- Archivos multimedia guardados en `media/`

## Notas

- La base de datos usada es SQLite en el archivo `db.sqlite3`.
- El proyecto está en modo `DEBUG = True`, no usar en producción sin adaptar seguridad.
- `STATICFILES_DIRS` incluye el directorio `static/` para CSS e imágenes.

## Uso

- Registra un usuario o ingresa con Google si está configurado.
- Compra planes desde `/planes/`.
- Administra planes y usuarios desde el panel administrativo si eres administrador.
- Crea y realiza rutinas desde el módulo de rutinas.
