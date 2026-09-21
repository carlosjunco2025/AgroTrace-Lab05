## Django Admin (Laboratorio 5)

Se registraron las 7 entidades del modelo de datos en el panel de administración de Django (`/admin/`):

- Registro simple: `CentroAcopio`, `VariedadCultivo`
- Registro con `ModelAdmin` personalizado: `CertificacionAgricola`, `FundoProductor`, `LoteRecepcionado`
- Registro simple (entidades de relaciones): `EvaluacionCalidadLote`, `CertificacionLote`

### Personalización de ModelAdmin

- `FundoProductorAdmin`: `list_display` (nombre, DNI/RUC, hectáreas) y `search_fields`.
- `LoteRecepcionadoAdmin`: `list_display` (código, fundo, toneladas, fecha), `search_fields` (incluyendo búsqueda a través de la FK con `fundo__nombre_fundo`) y `list_filter` (por fecha de ingreso y por fundo).
- `CertificacionAgricolaAdmin`: `list_display` y `search_fields`.

### Inlines

- `EvaluacionCalidadInline` (`StackedInline`): expone la relación 1:1 con `EvaluacionCalidadLote` dentro del formulario de `LoteRecepcionado`.
- `CertificacionLoteInline` (`TabularInline`): expone el modelo intermedio `CertificacionLote` de la relación N:M dentro del mismo formulario, mostrando `fecha_auditoria` y `codigo_inspeccion` como columnas editables.

Con esto, el flujo completo de creación, edición y eliminación de un lote y sus relaciones puede gestionarse desde una sola pantalla del Admin, sin necesidad de Views ni Templates propios para uso interno/staff.

## Instalación y ejecución

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd AgroTrace-Lab05

# Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario para acceder al panel de administración
python manage.py createsuperuser

# Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abrir en el navegador:
- `http://127.0.0.1:8000/agrotrace/fundos/`
- `http://127.0.0.1:8000/agrotrace/lotes/`
- `http://127.0.0.1:8000/agrotrace/certificaciones-lote/`
- `http://127.0.0.1:8000/admin/` (panel de administración — gestión completa de las 7 entidades con relaciones integradas mediante Inlines)