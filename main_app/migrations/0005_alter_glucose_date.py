# Generated by Django 4.0.2 on 2022-02-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_glucose_accucheck_glucose_insulin_patient_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glucose',
            name='date',
            field=models.DateField(verbose_name='glucose date'),
        ),
    ]
