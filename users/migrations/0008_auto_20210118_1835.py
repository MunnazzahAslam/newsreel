# Generated by Django 3.1.5 on 2021-01-18 18:35

from django.db import migrations, models
import imagekit.models.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_avatar_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=users.models.get_avatar_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=users.models.get_avatar_thumbnail_path),
        ),
    ]