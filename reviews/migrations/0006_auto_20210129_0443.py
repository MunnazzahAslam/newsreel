# Generated by Django 3.1.5 on 2021-01-29 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'Replies'},
        ),
        migrations.AlterField(
            model_name='reply',
            name='review',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reviews.review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='accuracy',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='contribution',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='ethics',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='expertise',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='fairness',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='trust',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
