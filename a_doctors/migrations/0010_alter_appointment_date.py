# Generated by Django 4.2.3 on 2023-08-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_doctors', '0009_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='%Y-%m-%d'),
        ),
    ]
