# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 09:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chubbies', '0004_auto_20151203_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='chubbie',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 3, 4, 47, 17, 489439)),
            preserve_default=False,
        ),
    ]
