# Generated by Django 4.0.1 on 2022-01-07 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_photo_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='pics/avatar.png', upload_to='pics'),
        ),
    ]