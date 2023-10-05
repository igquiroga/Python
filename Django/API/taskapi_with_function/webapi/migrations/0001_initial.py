# Generated by Django 4.1.3 on 2022-11-24 17:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosTareas',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('user_name', models.CharField(max_length=255, verbose_name='Usuario')),
                ('user_password', models.CharField(max_length=255, verbose_name='Contraseña')),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
