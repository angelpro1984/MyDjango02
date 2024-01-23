from django.contrib import admin


# Importar las clases del modelo
from administrativo.models import Docente, Materia

# Agregar la clase Docente para administrar desde
# interfaz de administración
# Previo a personalización
# admin.site.register(Docente)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Docente

class DocenteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)·
    # de la clase
    list_display=('cedula','nombres','apellido','titulo')
    search_fields = ('cedula', 'apellido', 'titulo')

# admin.site.register se lo altera
# el primer argumento es el modelo (Docente)
# el segundo argumento la clase DocenteAdmin

admin.site.register(Docente, DocenteAdmin)

# Agregar la clase Materia para administrar desde
# interfaz de administración
# antes de la personalización
# admin.site.register(Materia)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Materia
class MateriaAdmin(admin.ModelAdmin):
# listado de atributos que se mostrará
# por cada registro
# se deja de usar la representación (str)·
# de la clase·
    list_display=('nombre','docente')
# se agrega el atributo
# raw_id_fields que permite acceder a una interfaz·
# para buscar los docentes y seleccionar el que·
# se desee
raw_id_fields = ('docente',)

admin.site.register(Materia, MateriaAdmin)