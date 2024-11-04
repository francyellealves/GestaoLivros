# Generated by Django 5.1 on 2024-11-04 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_publicacao', models.DateField()),
                ('numero_paginas', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='biblioteca.autor')),
            ],
        ),
    ]
