# Generated by Django 4.2 on 2023-06-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
