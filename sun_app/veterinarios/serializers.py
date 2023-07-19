from rest_framework import serializers

from veterinarios.models import Veterinario


class vete_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'apellido', 'sexo', 'email', 'numero_celular', 'activo']