from django.contrib import admin
from .models import Autor, Libro

# Admin para el modelo Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad', 'fecha_nacimiento', 'mostrar_foto')
    search_fields = ('nombre', 'nacionalidad')
    list_filter = ('nacionalidad',)
    
    def mostrar_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.foto.url)
        return "Sin foto"
    mostrar_foto.short_description = 'Foto'

# Admin para el modelo Libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'año', 'autor', 'mostrar_portada')
    search_fields = ('titulo', 'genero', 'autor__nombre')
    list_filter = ('genero', 'año', 'autor')

    def mostrar_portada(self, obj):
        if obj.portada:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.portada.url)
        return "Sin portada"
    mostrar_portada.short_description = 'Portada'
