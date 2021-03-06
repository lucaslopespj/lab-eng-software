# Generated by Django 3.2.8 on 2021-10-22 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('estado_conservacao', models.TextField(choices=[('VELHO', 'VELHO'), ('SEMINOVO', 'SEMINOVO'), ('NOVO', 'NOVO')], default='VELHO')),
                ('valor_reserva', models.DecimalField(decimal_places=2, max_digits=11)),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('data_final', models.DateTimeField()),
                ('valor_lance_mais_alto', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('cliente_comprador_lance_mais_alto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cliente_vendedor', to=settings.AUTH_USER_MODEL)),
                ('cliente_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
