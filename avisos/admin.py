from django.contrib import admin
from .models import Avisos
# Register your models here.

class AvisosAdmin(admin.ModelAdmin):
    list_display = ('avi_id', 'avi_titulo', 'avi_descricao', 'avi_data', 'avi_arquivos', 'avi_administrador', "avi_mostrar")
    list_display_links = ('avi_titulo',)
    list_filter = ('avi_id', 'avi_titulo', 'avi_data')
    list_per_page = 10
    search_fields = ('avi_titulo',)
    list_editable = ('avi_descricao',)

admin.site.register(Avisos, AvisosAdmin)
