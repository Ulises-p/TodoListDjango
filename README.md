# TodoListDjango

Aplicación de lista de tareas (To-Do List) hecha con Django. Permite registrarse,
iniciar sesión y gestionar tareas propias (crear, ver, editar, eliminar y buscar).

## Requisitos

- Python 3.12 o superior.
  - Django 6.0 soporta Python 3.12, 3.13 y 3.14.
  - Si usas Python 3.15 necesitas Django 6.1.3 o superior (el rango de
    `requirements.txt` ya lo contempla).

## Instalación

1. Clona el repositorio y entra en la carpeta:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd TodoListDjango
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   ```

   - Windows (cmd/PowerShell):

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crea tu archivo de variables de entorno a partir del ejemplo:

   ```bash
   copy .env.example .env      # Windows
   cp .env.example .env        # macOS/Linux
   ```

   Edita `.env` y pon una `SECRET_KEY` propia. En desarrollo puedes dejar
   `DEBUG=True`.

5. Aplica las migraciones (esto crea la base de datos SQLite `db.sqlite3`):

   ```bash
   python manage.py migrate
   ```

6. (Opcional) Crea un superusuario para el panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Arranca el servidor:

   ```bash
   python manage.py runserver
   ```

   Abre `http://127.0.0.1:8000/` en el navegador.

## Estructura del proyecto

```
TodoListDjango/
├── manage.py
├── requirements.txt
├── .env.example
├── base/                  # App con la lógica de las tareas
│   ├── migrations/
│   ├── templates/base/    # Plantillas HTML
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── TodoListDjango/        # Configuración del proyecto
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Notas

- `db.sqlite3` y el archivo `.env` no se suben al repositorio (están en
  `.gitignore`). Cada persona genera los suyos con los pasos anteriores.
- Para producción: pon `DEBUG=False`, define `ALLOWED_HOSTS` y usa una
  `SECRET_KEY` segura.
