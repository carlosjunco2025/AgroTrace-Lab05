## Refactorización de Templates, Modularidad y Seguridad (Laboratorio 6)

Se refactorizó la capa de presentación (Templates) para todas las entidades del proyecto `AgroTrace`, aplicando herencia de plantillas, componentes modulares reusables, filtros de formato nativos y verificación de seguridad contra vulnerabilidades XSS.

- **Herencia de Plantillas (`base.html`)**: Migración de las plantillas de `FundoProductor`, `LoteRecepcionado` y entidades de la investigación propia para extender de un layout maestro unificado mediante `{% extends %}` y `{% block content %}`.
- **Modularización (`{% include %}`)**: Extracción de componentes visuales repetidos hacia plantillas independientes, incluyendo la cabecera dinámica global (`header.html`) y tarjetas de presentación para relaciones intermedias N:M (`relacion_card.html`).
- **Filtros de Formato (Template Filters)**: Aplicación de filtros nativos como `|upper` para texto en mayúsculas, `|date:"d/m/Y"` para formato de fechas, `|floatformat` para precisión en toneladas/hectáreas y `|default` para atributos no especificados.

### Seguridad y Verificación (Auto-Escape XSS)

- **Sanitización Nativa**: Se probó la inyección de vectores de script (`<script>alert("XSS Test")</script>`) en los formularios de creación de datos (`LoteRecepcionado`).
- **Confirmación en el DOM**: Se verificó a través del inspector de elementos (**F12**) que el motor de plantillas de Django transforma automáticamente los caracteres `<` y `>` en entidades HTML seguras (`&lt;` y `&gt;`), previniendo ataques de Cross-Site Scripting sin requerir bibliotecas externas.

### Refactorización por Entidades

- `FundoProductor`: Renderizado dinámico con tabla estilizada Bootstrap 5, acciones rápidas de edición/eliminación y formateo de hectáreas.
- `LoteRecepcionado`: Despliegue de relaciones 1:N (`Fundo`), 1:1 (`EvaluacionCalidad`) y N:M (`Certificaciones`) con filtros de formato en toneladas y porcentajes de descarte.
- `CertificacionAgricola` / `EvaluacionCalidadLote`: Integración de tarjetas modulares `relacion_card.html` para presentación clara de registros.

Con esto, el sistema AgroTrace cuenta con una interfaz de usuario final completamente funcional, mantenible y segura, complementando la gestión interna realizada previamente en el Django Admin.

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone [https://github.com/carlosjunco2025/agrotrace.git](https://github.com/carlosjunco2025/agrotrace.git)
cd agrotrace

# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario para acceder al panel de administración
python manage.py createsuperuser

# Levantar el servidor de desarrollo
python manage.py runserver

Luego abrir en el navegador:

http://127.0.0.1:8000/agrotrace/fundos/ (gestión refactorizada de fundos)

http://127.0.0.1:8000/agrotrace/lotes/ (gestión refactorizada de lotes)

http://127.0.0.1:8000/admin/ (panel de administración de Django)


---
