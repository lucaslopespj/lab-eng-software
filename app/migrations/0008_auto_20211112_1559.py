# Generated by Django 3.2.9 on 2021-11-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_pagamento_tipo_de_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='autor',
            field=models.CharField(default='Professor USP', max_length=200),
        ),
        migrations.AddField(
            model_name='lote',
            name='editora',
            field=models.CharField(default='Editora USP', max_length=200),
        ),
        migrations.AddField(
            model_name='lote',
            name='numero_de_paginas',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
    ]
