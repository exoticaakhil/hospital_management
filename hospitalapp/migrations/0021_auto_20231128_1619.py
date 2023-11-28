# Generated by Django 3.0.5 on 2023-11-28 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0020_auto_20231128_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment1',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Doctor'),
        ),
        migrations.AlterField(
            model_name='appointment1',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.Patient'),
        ),
    ]