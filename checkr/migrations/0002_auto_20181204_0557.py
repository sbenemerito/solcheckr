# Generated by Django 2.1.3 on 2018-12-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githubaudit',
            name='files_directory',
        ),
        migrations.AddField(
            model_name='githubaudit',
            name='contracts',
            field=models.TextField(blank=True, default=''),
        ),
    ]