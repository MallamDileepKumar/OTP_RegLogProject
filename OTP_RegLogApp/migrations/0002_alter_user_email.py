# Generated by Django 4.2.4 on 2023-10-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTP_RegLogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
