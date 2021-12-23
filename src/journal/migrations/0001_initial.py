 # Generated by Django 3.2.9 on 2021-12-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_path', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
