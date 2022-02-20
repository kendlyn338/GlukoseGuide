# Generated by Django 4.0.2 on 2022-02-20 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_patient_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glucose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='glucose date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('HS', 'Bedtime')], default='B', max_length=2)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
