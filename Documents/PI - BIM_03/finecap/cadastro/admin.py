from django.contrib import admin
from .models import Stand, Reserva
# Register your models here.

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display=('localizacao',)

