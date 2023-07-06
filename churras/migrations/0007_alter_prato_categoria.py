# Generated by Django 4.2.2 on 2023-07-06 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churras', '0006_alter_prato_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='categoria',
            field=models.CharField(choices=[('Churrasco', 'Churrasco'), ('Entrada', 'Entrada'), ('Sobremesa', 'Sobremesa')], max_length=100, verbose_name='Categoria'),
        ),
    ]
