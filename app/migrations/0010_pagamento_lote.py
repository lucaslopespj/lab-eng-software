# Generated by Django 3.2.9 on 2021-11-18 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211112_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='lote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.lote'),
        ),
    ]
