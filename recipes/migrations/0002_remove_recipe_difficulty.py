# Generated by Django 5.0.3 on 2024-03-21 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty',
        ),
    ]
