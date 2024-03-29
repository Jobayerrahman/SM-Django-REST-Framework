# Generated by Django 4.2.9 on 2024-01-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=60)),
                ('doctor_speciality', models.CharField(max_length=60)),
                ('doctor_schedule', models.TimeField()),
                ('doctor_visit', models.IntegerField()),
            ],
        ),
    ]
