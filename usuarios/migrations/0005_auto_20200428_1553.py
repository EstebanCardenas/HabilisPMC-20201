# Generated by Django 2.2 on 2020-04-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20200428_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='user_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]