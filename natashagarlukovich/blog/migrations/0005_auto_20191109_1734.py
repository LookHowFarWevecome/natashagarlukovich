# Generated by Django 2.2.6 on 2019-11-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191109_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
