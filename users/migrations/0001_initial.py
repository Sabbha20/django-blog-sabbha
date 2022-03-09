# Generated by Django 4.0.1 on 2022-01-06 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('U', 'Undefined'), ('F', 'Female'), ('M', 'Male'), ('T', 'Transgender')], max_length=2)),
                ('bio', models.CharField(blank=True, max_length=160, null=True)),
                ('photo', models.ImageField(upload_to='pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
