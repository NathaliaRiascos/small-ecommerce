# Generated by Django 3.2.4 on 2021-07-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_remove_categoria_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=110, verbose_name='Descripción'),
        ),
    ]
