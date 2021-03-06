# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 19:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Telefone deve ser numérico', regex='^[0-9]+$'), django.core.validators.RegexValidator(message='Telefone deve ter pelo menos 9 dígitos', regex='^[0-9]{9,15}$')])),
                ('sexo', models.CharField(choices=[('N', 'Não Informado'), ('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default='N', max_length=1)),
                ('site', models.URLField(null=True)),
            ],
        ),
    ]
