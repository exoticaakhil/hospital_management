# Generated by Django 3.0.5 on 2023-11-28 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0015_auto_20231128_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacy',
            old_name='Patient_id',
            new_name='Patientno',
        ),
    ]