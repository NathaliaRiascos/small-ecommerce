# Generated by Django 3.2.4 on 2021-07-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_auto_20210702_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default='cosmeticos', max_length=100, verbose_name='Slug'),
        ),
    ]
