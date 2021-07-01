# Generated by Django 3.2.4 on 2021-06-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='anime.anime'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='anime.anime'),
        ),
    ]