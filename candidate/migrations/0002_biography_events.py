# Generated by Django 5.0.7 on 2024-08-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biography',
            name='events',
            field=models.TextField(),
        ),
    ]
