# Generated by Django 3.2.8 on 2021-11-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211102_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saldo',
            name='cliente',
        ),
        migrations.AddField(
            model_name='saldo',
            name='username_cliente',
            field=models.CharField(default='man', max_length=150),
            preserve_default=False,
        ),
    ]
