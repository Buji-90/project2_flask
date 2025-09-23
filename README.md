# User Manager – Flask (CRUD + Validaciones)

Aplicación web en **Flask** para la gestión de usuarios con **arquitectura por capas** (models, services, data_access), persistencia en **JSON**, validaciones de negocio y vistas HTML estilizadas con CSS.

Incluye endpoints REST y plantillas Jinja2 para interacción desde navegador.

---

## 🚀 Stack
- Python 3.11+
- Flask 3.x + flask-ngrok (para demo)
- Jinja2 (templates)
- CSS (estilos)
- Persistencia en JSON (plan futuro: SQLite + SQLAlchemy)

---

## 📂 Estructura del proyecto
├── app.py # entrypoint con endpoints y vistas
├── models.py # clase User (POO)
├── services.py # lógica de negocio y validaciones
├── data_access.py # persistencia en JSON
├── requirements.txt
├── .gitignore
├── data/
│ └── users.json # se crea automáticamente
├── templates/
│ ├── base.html
│ ├── form.html
│ ├── menu.html
│ └── tabla.html
└── static/
└── css/
└── styles.css

---

## ⚙️ Instalación
```bash
# Clonar repositorio
git clone https://github.com/Buji-90/project2_flask.git

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

# Instalar dependencias
pip install -r requirements.txt
