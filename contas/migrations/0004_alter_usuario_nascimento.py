# Generated by Django 5.1.6 on 2025-02-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_alter_usuario_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
