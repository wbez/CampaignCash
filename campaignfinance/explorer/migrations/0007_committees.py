# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0006_auto_20150210_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmterefername', models.TextField(db_column=b'CmteReferName', blank=True)),
                ('statecmte', models.NullBooleanField(db_column=b'StateCmte')),
                ('stateid', models.IntegerField(null=True, db_column=b'StateID', blank=True)),
                ('localcmte', models.NullBooleanField(db_column=b'LocalCmte')),
                ('localid', models.IntegerField(null=True, db_column=b'LocalID', blank=True)),
                ('cmtename', models.TextField(db_column=b'CmteName', blank=True)),
                ('address1', models.TextField(db_column=b'Address1', blank=True)),
                ('address2', models.TextField(db_column=b'Address2', blank=True)),
                ('address3', models.TextField(db_column=b'Address3', blank=True)),
                ('city', models.TextField(db_column=b'City', blank=True)),
                ('state', models.TextField(db_column=b'State', blank=True)),
                ('zip', models.TextField(db_column=b'Zip', blank=True)),
                ('status', models.TextField(db_column=b'Status', blank=True)),
                ('statusdate', models.DateField(null=True, db_column=b'StatusDate', blank=True)),
                ('typeofcommittee', models.TextField(db_column=b'TypeOfCommittee', blank=True)),
            ],
            options={
                'db_table': 'committees',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
