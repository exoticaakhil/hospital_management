# Generated by Django 3.0.5 on 2023-11-24 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospitalapp', '0008_remove_doctor_user_remove_patient_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='username',
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patient1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]