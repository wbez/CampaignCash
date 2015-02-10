# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0004_appcommittee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appcandidate',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appcommittee',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='slug',
            field=models.SlugField(default='default'),
            preserve_default=False,
        ),
    ]
