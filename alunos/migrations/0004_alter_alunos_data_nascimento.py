# Generated by Django 5.0.4 on 2024-04-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0003_remove_alunos_foto_alunos_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='data_nascimento',
            field=models.CharField(max_length=20),
        ),
    ]
