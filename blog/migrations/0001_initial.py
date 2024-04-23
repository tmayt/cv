# Generated by Django 5.0.4 on 2024-04-22 15:59

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blog')),
                ('date_update', models.DateField(auto_now=True)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('tags', models.TextField(help_text='split keyword by comma')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
        ),
    ]
