# Generated by Django 4.1.7 on 2023-06-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=150)),
                ('website', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('storyline', models.CharField(max_length=500)),
                ('status_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
