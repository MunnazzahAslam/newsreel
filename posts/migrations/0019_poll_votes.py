# Generated by Django 3.1.5 on 2021-03-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20210301_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='votes',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
