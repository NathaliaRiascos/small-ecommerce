# Generated by Django 3.2.4 on 2021-07-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(max_length=200, upload_to='img_product/', verbose_name='Imagen de producto'),
        ),
    ]
