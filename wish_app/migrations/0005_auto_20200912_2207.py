# Generated by Django 2.2 on 2020-09-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0004_auto_20200912_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishes',
            name='like',
        ),
        migrations.AddField(
            model_name='wishes',
            name='granted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Granted',
        ),
    ]
