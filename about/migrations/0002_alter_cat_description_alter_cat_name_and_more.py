# Generated by Django 4.2 on 2023-05-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.CharField(max_length=350, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Breed'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='temperament',
            field=models.CharField(max_length=150, verbose_name='Temperament'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='wikipedia_url',
            field=models.CharField(max_length=150, verbose_name='Url'),
        ),
    ]
