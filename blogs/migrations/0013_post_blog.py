# Generated by Django 2.1.5 on 2019-02-26 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_auto_20190226_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.TextField(null=True),
        ),
    ]
