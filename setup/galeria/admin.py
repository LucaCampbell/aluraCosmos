from django.contrib import admin

from .models import Fotografia, Usuario


class ListandoFoto(admin.ModelAdmin):
    list_display = ('id', 'nome_foto', 'categoria')
    list_display_links = ('id', 'nome_foto')
    search_fields = ('nome_foto',)
    list_filter = ('categoria',)
    list_per_page = 20


class ListandoUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Fotografia, ListandoFoto)
admin.site.register(Usuario, ListandoUsuario)
