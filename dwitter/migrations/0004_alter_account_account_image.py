# Generated by Django 4.1.5 on 2023-01-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0003_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
