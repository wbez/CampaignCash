# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0005_auto_20150209_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='appcandidate',
            name='bio',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appcandidate',
            name='nameMiddle',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='race',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appcandidate',
            name='nameFirst',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appcandidate',
            name='nameLast',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='appcommittee',
            name='candidate',
            field=models.ForeignKey(to='explorer.AppCandidate', null=True),
            preserve_default=True,
        ),
    ]
