from django.contrib import admin
from .models import Tipo, Lead, Operadora

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Operadora)
admin.site.register(Lead)

