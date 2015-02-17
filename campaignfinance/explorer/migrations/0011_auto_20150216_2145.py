# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0010_auto_20150211_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcommittee',
            name='committeeid',
            field=models.IntegerField(serialize=False, primary_key=True, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='race',
            name='ward',
            field=models.IntegerField(unique=True, max_length=2, db_index=True),
            preserve_default=True,
        ),
    ]
