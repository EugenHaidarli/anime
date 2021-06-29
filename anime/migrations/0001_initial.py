# Generated by Django 3.2.4 on 2021-06-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_series', models.BooleanField(default=True)),
                ('episodes', models.IntegerField(blank=True)),
                ('cover', models.FilePathField()),
            ],
        ),
    ]
