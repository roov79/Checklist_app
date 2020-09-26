# Generated by Django 2.2 on 2020-09-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0002_wishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishes',
            name='granted',
            field=models.ManyToManyField(related_name='granted', to='wish_app.Users'),
        ),
        migrations.AddField(
            model_name='wishes',
            name='like',
            field=models.ManyToManyField(related_name='likes', to='wish_app.Users'),
        ),
    ]
