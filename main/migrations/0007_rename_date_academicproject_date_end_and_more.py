# Generated by Django 4.2.7 on 2024-01-07 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_academicproject_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicproject',
            old_name='date',
            new_name='date_end',
        ),
        migrations.AddField(
            model_name='academicproject',
            name='date_start',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='academicproject',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='main.academicprojectcategory'),
        ),
    ]
