# Generated by Django 3.1.5 on 2021-03-01 14:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0017_auto_20210301_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='voters',
            field=models.ManyToManyField(related_name='post_voters', to=settings.AUTH_USER_MODEL),
        ),
    ]