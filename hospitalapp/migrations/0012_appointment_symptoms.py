# Generated by Django 3.0.5 on 2023-11-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_appointment1_symptoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Symptoms',
            field=models.CharField(max_length=255, null=True),
        ),
    ]