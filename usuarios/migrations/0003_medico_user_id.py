# Generated by Django 2.2 on 2020-04-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200428_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]