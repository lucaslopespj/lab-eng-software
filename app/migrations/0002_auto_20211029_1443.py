# Generated by Django 3.2.8 on 2021-10-29 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='valor_minimo_incremento_por_lance',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=11),
        ),
        migrations.AddField(
            model_name='lote',
            name='valor_minimo_lance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
