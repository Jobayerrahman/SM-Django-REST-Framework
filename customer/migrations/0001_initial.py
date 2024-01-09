# Generated by Django 4.2.9 on 2024-01-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=60)),
                ('customer_address', models.CharField(max_length=60)),
                ('customer_contact', models.CharField(max_length=60)),
                ('customer_due', models.IntegerField()),
            ],
        ),
    ]