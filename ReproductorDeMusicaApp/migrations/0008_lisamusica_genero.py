# Generated by Django 2.2.3 on 2021-01-31 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReproductorDeMusicaApp', '0007_remove_lisamusica_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='lisamusica',
            name='genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ReproductorDeMusicaApp.Genero'),
        ),
    ]