# Generated by Django 3.2.4 on 2021-07-02 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_usuario_usuario_moderador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario_moderador',
        ),
    ]
