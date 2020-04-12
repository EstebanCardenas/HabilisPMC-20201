# Generated by Django 2.2 on 2020-04-12 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('eps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Paciente'),
        ),
    ]