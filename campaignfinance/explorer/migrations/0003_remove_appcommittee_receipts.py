# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_auto_20150208_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appcommittee',
            name='receipts',
        ),
    ]
