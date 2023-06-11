# Generated by Django 4.2.1 on 2023-05-31 19:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Category Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
    ]