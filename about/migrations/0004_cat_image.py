# Generated by Django 4.2 on 2023-06-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='image',
            field=models.ImageField(default='Aegean_Island_Cat.jpg', upload_to='cat_images/'),
        ),
    ]