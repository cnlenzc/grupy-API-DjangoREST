from rest_framework import serializers
from client_app.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
   class Meta:
        model = Cliente
        fields = ('__all__')
