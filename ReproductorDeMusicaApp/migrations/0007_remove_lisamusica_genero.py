# Generated by Django 2.2.3 on 2021-01-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReproductorDeMusicaApp', '0006_lisamusica_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lisamusica',
            name='genero',
        ),
    ]
