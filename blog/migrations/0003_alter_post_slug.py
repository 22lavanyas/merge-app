# Generated by Django 4.2.7 on 2024-04-23 12:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]