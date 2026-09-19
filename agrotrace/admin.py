from django.contrib import admin
from .models import (
    CentroAcopio, 
    VariedadCultivo, 
    CertificacionAgricola, 
    FundoProductor, 
    LoteRecepcionado,
    EvaluacionCalidadLote,
    CertificacionLote  # Importado en Ejercicio 7
)

# ==============================================================================
# EJERCICIO 3 — Registrar modelos básicos
# ==============================================================================
admin.site.register(CentroAcopio)
admin.site.register(VariedadCultivo)
admin.site.register(CertificacionAgricola)


# ==============================================================================
# EJERCICIO 6 — Exponer la relación 1:1 con StackedInline
# ==============================================================================
class EvaluacionCalidadInline(admin.StackedInline):
    model = EvaluacionCalidadLote
    extra = 1


# ==============================================================================
# EJERCICIO 7 — Exponer la relación N:M con TabularInline (modelo intermedio)
# ==============================================================================
class CertificacionLoteInline(admin.TabularInline):
    model = CertificacionLote
    extra = 1


# ==============================================================================
# EJERCICIO 4 — Personalizar con ModelAdmin (FundoProductor)
# ==============================================================================
@admin.register(FundoProductor)
class FundoProductorAdmin(admin.ModelAdmin):
    list_display = ('nombre_fundo', 'propietario_dni_ruc', 'hectareas')  # Ejercicio 4
    search_fields = ('nombre_fundo', 'propietario_dni_ruc')               # Ejercicio 4


# ==============================================================================
# EJERCICIOS 4, 5, 6 y 7 — Personalización completa de LoteRecepcionado
# ==============================================================================
@admin.register(LoteRecepcionado)
class LoteRecepcionadoAdmin(admin.ModelAdmin):
    # Ejercicio 4: Columnas personalizadas
    list_display = ('codigo_lote', 'fundo', 'toneladas_brutas', 'fecha_ingreso')
    
    # Ejercicio 4: Barra de búsqueda
    search_fields = ('codigo_lote', 'fundo__nombre_fundo')
    
    # Ejercicio 5: Panel lateral de filtros
    list_filter = ('fecha_ingreso', 'fundo')
    
    # Ejercicios 6 y 7: Formularios integrados (1:1 en bloque y N:M en tabla)
    inlines = [EvaluacionCalidadInline, CertificacionLoteInline]