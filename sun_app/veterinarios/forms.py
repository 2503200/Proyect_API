from django.forms import EmailInput, ModelForm

from veterinarios.models import Veterinario


class VeterinarioFormulario(ModelForm):
    class Meta:
        model = Veterinario
        fields = ('nombre', 'apellido', 'sexo', 'email', 'numero_celular', 'activo', 'consultorio', 'especialidad', 'horario')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }