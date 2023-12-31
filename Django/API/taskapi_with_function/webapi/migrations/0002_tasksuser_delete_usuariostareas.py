# Generated by Django 4.1.3 on 2022-11-24 18:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='user_id')),
                ('user_name', models.CharField(max_length=255, verbose_name='user_name')),
                ('user_password', models.CharField(max_length=255, verbose_name='user_password')),
            ],
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='UsuariosTareas',
        ),
    ]
