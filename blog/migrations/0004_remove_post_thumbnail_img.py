# Generated by Django 2.2.4 on 2019-08-09 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_thumbnail_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumbnail_img',
        ),
    ]