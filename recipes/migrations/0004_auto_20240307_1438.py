# Generated by Django 2.2.28 on 2024-03-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favourite_recipes',
            field=models.TextField(blank=True),
        ),
    ]