# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0003_remove_appcommittee_receipts'),
    ]

    operations = [
        migrations.AddField(
            model_name='appcommittee',
            name='name',
            field=models.CharField(default='Chicago for Rahm Emanuel', unique=True, max_length=128),
            preserve_default=False,
        ),
    ]
