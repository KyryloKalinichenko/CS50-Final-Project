# Generated by Django 3.2.7 on 2021-11-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20211124_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='link',
            field=models.TextField(default=0, max_length=300),
        ),
    ]
