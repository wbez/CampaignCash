# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0007_committees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcommittee',
            name='name',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
