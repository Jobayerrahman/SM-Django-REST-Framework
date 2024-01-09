# Generated by Django 4.2.9 on 2024-01-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_code', models.CharField(max_length=60)),
                ('investor_name', models.CharField(max_length=60)),
                ('investor_contact', models.CharField(max_length=80)),
                ('investment_amount', models.CharField(max_length=60)),
            ],
        ),
    ]
