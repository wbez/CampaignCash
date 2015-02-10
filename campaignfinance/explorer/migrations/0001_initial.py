# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('committeeid', models.IntegerField(db_column=b'CommitteeID', blank=True)),
                ('lastonlyname', models.TextField(db_column=b'LastOnlyName', blank=True)),
                ('firstname', models.TextField(db_column=b'FirstName', blank=True)),
                ('rcvdate', models.DateField(null=True, db_column=b'RcvDate', blank=True)),
                ('amount', models.FloatField(null=True, db_column=b'Amount', blank=True)),
                ('loanamount', models.FloatField(null=True, db_column=b'LoanAmount', blank=True)),
                ('occupation', models.TextField(db_column=b'Occupation', blank=True)),
                ('employer', models.TextField(db_column=b'Employer', blank=True)),
                ('address1', models.TextField(db_column=b'Address1', blank=True)),
                ('address2', models.TextField(db_column=b'Address2', blank=True)),
                ('city', models.TextField(db_column=b'City', blank=True)),
                ('state', models.TextField(db_column=b'State', blank=True)),
                ('zip', models.TextField(db_column=b'Zip', blank=True)),
                ('rcttype', models.TextField(db_column=b'RctType', blank=True)),
                ('description', models.TextField(db_column=b'Description', blank=True)),
                ('vendorlastonlyname', models.TextField(db_column=b'VendorLastOnlyName', blank=True)),
                ('vendorfirstname', models.TextField(db_column=b'VendorFirstName', blank=True)),
                ('vendoraddress1', models.TextField(db_column=b'VendorAddress1', blank=True)),
                ('vendoraddress2', models.TextField(db_column=b'VendorAddress2', blank=True)),
                ('vendorcity', models.TextField(db_column=b'VendorCity', blank=True)),
                ('vendorstate', models.TextField(db_column=b'VendorState', blank=True)),
                ('vendorzip', models.TextField(db_column=b'VendorZip', blank=True)),
                ('rpttype', models.TextField(db_column=b'RptType', blank=True)),
                ('electiontype', models.TextField(db_column=b'ElectionType', blank=True)),
                ('electionyear', models.TextField(db_column=b'ElectionYear', blank=True)),
                ('rptpdbegdate', models.TextField(null=True, db_column=b'RptPdBegDate', blank=True)),
                ('rptpdenddate', models.DateField(null=True, db_column=b'RptPdEndDate', blank=True)),
                ('rptrcvddate', models.DateTimeField(null=True, db_column=b'RptRcvdDate', blank=True)),
                ('cmterefername', models.TextField(db_column=b'CmteReferName', blank=True)),
                ('cmtename', models.TextField(db_column=b'CmteName', blank=True)),
                ('statecmte', models.NullBooleanField(db_column=b'StateCmte')),
                ('stateid', models.IntegerField(null=True, db_column=b'StateID', blank=True)),
                ('localcmte', models.NullBooleanField(db_column=b'LocalCmte')),
                ('localid', models.IntegerField(null=True, db_column=b'LocalID', blank=True)),
                ('id', models.BigIntegerField(unique=True, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'receipts',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppCandidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameFirst', models.CharField(unique=True, max_length=128)),
                ('nameLast', models.CharField(unique=True, max_length=128)),
                ('incumbant', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppCommittee',
            fields=[
                ('committeeid', models.IntegerField(serialize=False, primary_key=True, db_column=b'CommitteeID', blank=True)),
                ('candidate', models.ForeignKey(to='explorer.AppCandidate')),
                ('receipts', models.ManyToManyField(to='explorer.Receipts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('ward', models.IntegerField(unique=True, max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appcandidate',
            name='races',
            field=models.ManyToManyField(to='explorer.Race'),
            preserve_default=True,
        ),
    ]
