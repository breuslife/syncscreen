# Generated by Django 4.1.3 on 2022-11-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
