from django.contrib import admin

from .models import Comprador,Leiloeiro,Vendedor

admin.site.register(Comprador)
admin.site.register(Leiloeiro)
admin.site.register(Vendedor)
