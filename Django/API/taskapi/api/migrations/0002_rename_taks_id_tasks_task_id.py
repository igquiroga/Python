# Generated by Django 4.1.3 on 2022-11-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='taks_id',
            new_name='task_id',
        ),
    ]
