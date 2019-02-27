# Generated by Django 2.1.5 on 2019-02-27 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20190226_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Author'),
        ),
    ]
