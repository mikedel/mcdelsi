# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chubbies', '0002_chubbie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chubbie',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]