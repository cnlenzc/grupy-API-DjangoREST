from django.db.models import Model, CharField, EmailField, URLField
from django.core.validators import RegexValidator

enum_sexo = (('N', 'Não Informado'), ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'))
telefone_validators = [
    RegexValidator(regex='^[0-9]+$', message='Telefone deve ser numérico'),
    RegexValidator(regex='^[0-9]{9,15}$', message='Telefone deve ter pelo menos 9 dígitos')]

class Cliente(Model):
    nome     = CharField(max_length=50)
    email    = EmailField(unique=True, db_index=True)
    telefone = CharField(max_length=15, null=True, validators=telefone_validators)
    sexo     = CharField(choices=enum_sexo, max_length=1, default='N')
    site     = URLField(null=True)
