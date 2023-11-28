# Generated by Django 3.0.5 on 2023-11-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0018_auto_20231128_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='Patientno',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='Patient',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appointment1',
            name='doctor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='appointment1',
            name='patient',
            field=models.CharField(max_length=255, null=True),
        ),
    ]