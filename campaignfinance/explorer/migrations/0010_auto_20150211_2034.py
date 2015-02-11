# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0009_auto_20150210_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appcandidate',
            options={'ordering': ['nameLast']},
        ),
    ]
