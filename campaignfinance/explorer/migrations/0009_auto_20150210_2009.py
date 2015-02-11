# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0008_auto_20150210_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcommittee',
            name='name',
            field=models.TextField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appcommittee',
            name='slug',
            field=models.SlugField(max_length=255),
            preserve_default=True,
        ),
    ]
