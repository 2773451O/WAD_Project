# Generated by Django 2.2.28 on 2024-03-19 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(to='recipes.Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
