# Generated by Django 3.2.9 on 2021-12-23 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='article_path',
        ),
        migrations.AddField(
            model_name='articles',
            name='article',
            field=models.FileField(default=django.utils.timezone.now, max_length=1000, upload_to='articles/'),
            preserve_default=False,
        ),
    ]