# Generated by Django 3.1.4 on 2020-12-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_auto_20201208_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='star',
        ),
        migrations.DeleteModel(
            name='AnimeShots',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingStar',
        ),
    ]
