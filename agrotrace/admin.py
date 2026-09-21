from django.contrib import admin
from .models import (
    CentroAcopio, 
    VariedadCultivo, 
    CertificacionAgricola, 
    FundoProductor, 
    LoteRecepcionado,
    EvaluacionCalidadLote,
    CertificacionLote
)

# ==============================================================================
# EJERCICIO 9 — Registrar las 7 entidades
# ==============================================================================

# Registro simple
admin.site.register(CentroAcopio)
admin.site.register(VariedadCultivo)

# Registro con ModelAdmin (tercer modelo personalizado, además de Fundo y Lote)
@admin.register(CertificacionAgricola)
class CertificacionAgricolaAdmin(admin.ModelAdmin):
    list_display = ('nombre_certificacion', 'entidad_emisora')
    search_fields = ('nombre_certificacion',)

# Entidades de las relaciones, registradas también de forma independiente
admin.site.register(EvaluacionCalidadLote)
admin.site.register(CertificacionLote)


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
    list_display = ('nombre_fundo', 'propietario_dni_ruc', 'hectareas')
    search_fields = ('nombre_fundo', 'propietario_dni_ruc')


# ==============================================================================
# EJERCICIOS 4, 5, 6 y 7 — Personalización completa de LoteRecepcionado
# ==============================================================================
@admin.register(LoteRecepcionado)
class LoteRecepcionadoAdmin(admin.ModelAdmin):
    list_display = ('codigo_lote', 'fundo', 'toneladas_brutas', 'fecha_ingreso')
    search_fields = ('codigo_lote', 'fundo__nombre_fundo')
    list_filter = ('fecha_ingreso', 'fundo')
    inlines = [EvaluacionCalidadInline, CertificacionLoteInline]