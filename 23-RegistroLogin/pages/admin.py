from django.contrib import admin
from .models import Page

#Configuracion Extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

#Configuracion del panel
title = 'Panel de Gestion'
subtitle = 'Proyecto con Django'

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle