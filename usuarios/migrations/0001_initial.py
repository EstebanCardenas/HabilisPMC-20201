# Generated by Django 3.0.4 on 2020-04-13 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.BigIntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Usuario')),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('eps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eps.Eps')),
            ],
            bases=('usuarios.usuario',),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuarios.Usuario')),
                ('regMedico', models.CharField(blank=True, max_length=100, null=True)),
                ('edad', models.SmallIntegerField(blank=True, null=True)),
                ('especialidad', models.CharField(blank=True, max_length=120, null=True)),
                ('eps', models.ManyToManyField(blank=True, to='eps.Eps')),
            ],
            bases=('usuarios.usuario',),
        ),
    ]
