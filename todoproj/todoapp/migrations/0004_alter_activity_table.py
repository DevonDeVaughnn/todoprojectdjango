# Generated by Django 3.2 on 2021-06-09 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_task_activity_title'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='activity',
            table='activities',
        ),
    ]