# Generated by Django 3.2.8 on 2021-10-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211029_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='lote',
            name='taxa_cancelamento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
    ]
