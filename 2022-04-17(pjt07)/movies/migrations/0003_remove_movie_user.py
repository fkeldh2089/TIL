# Generated by Django 3.2.11 on 2022-04-15 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
    ]