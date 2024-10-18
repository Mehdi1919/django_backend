# Generated by Django 5.1.2 on 2024-10-17 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('agreement', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=100)),
                ('cnic', models.CharField(max_length=15)),
                ('comment', models.TextField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('hobby', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='profile_images/')),
                ('phone', models.CharField(max_length=15)),
                ('postalCode', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]