# Generated by Django 4.2.6 on 2024-02-28 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('Employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Employee_name', models.CharField(max_length=20)),
                ('Employee_mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('Employee_email', models.EmailField(max_length=50)),
                ('Employee_dob', models.DateField()),
            ],
        ),
    ]
