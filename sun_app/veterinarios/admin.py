from django.contrib import admin

from veterinarios.models import Veterinario, Consultorio, Especialidad, Horario

# Register your models here.
admin.site.register(Veterinario)
admin.site.register(Consultorio)
admin.site.register(Especialidad)
admin.site.register(Horario)