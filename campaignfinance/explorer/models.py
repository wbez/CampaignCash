from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ward = models.IntegerField(max_length=2, unique=True)

    def __unicode__(self):
        return self.name

class AppCandidate(models.Model):
	races = models.ManyToManyField(Race)
	nameFirst = models.CharField(max_length=128, unique=True)
	nameLast = models.CharField(max_length=128, unique=True)
	incumbant = models.BooleanField(default=False)

	def __unicode__(self):
		return '%s %s' % (self.nameFirst, self.nameLast)

class AppCommittee(models.Model):
	committeeid = models.IntegerField(primary_key=True)
	candidate = models.ForeignKey(AppCandidate)

	def _get_all_contributions(self):
		"Returns the sum of contributions for this committee"
		return self.receipts_set.aggregate(Sum('amount'))
	sum_contributions = property(_get_all_contributions)

	def __unicode__(self):
		return '%s: %s' % (self.committeeid, self.candidate)

class Receipts(models.Model):
    committeeid = models.ForeignKey(AppCommittee,db_column='CommitteeID')  # Field name made lowercase.
    lastonlyname = models.TextField(db_column='LastOnlyName', blank=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True)  # Field name made lowercase.
    rcvdate = models.DateField(db_column='RcvDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    loanamount = models.FloatField(db_column='LoanAmount', blank=True, null=True)  # Field name made lowercase.
    occupation = models.TextField(db_column='Occupation', blank=True)  # Field name made lowercase.
    employer = models.TextField(db_column='Employer', blank=True)  # Field name made lowercase.
    address1 = models.TextField(db_column='Address1', blank=True)  # Field name made lowercase.
    address2 = models.TextField(db_column='Address2', blank=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True)  # Field name made lowercase.
    zip = models.TextField(db_column='Zip', blank=True)  # Field name made lowercase.
    rcttype = models.TextField(db_column='RctType', blank=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True)  # Field name made lowercase.
    vendorlastonlyname = models.TextField(db_column='VendorLastOnlyName', blank=True)  # Field name made lowercase.
    vendorfirstname = models.TextField(db_column='VendorFirstName', blank=True)  # Field name made lowercase.
    vendoraddress1 = models.TextField(db_column='VendorAddress1', blank=True)  # Field name made lowercase.
    vendoraddress2 = models.TextField(db_column='VendorAddress2', blank=True)  # Field name made lowercase.
    vendorcity = models.TextField(db_column='VendorCity', blank=True)  # Field name made lowercase.
    vendorstate = models.TextField(db_column='VendorState', blank=True)  # Field name made lowercase.
    vendorzip = models.TextField(db_column='VendorZip', blank=True)  # Field name made lowercase.
    rpttype = models.TextField(db_column='RptType', blank=True)  # Field name made lowercase.
    electiontype = models.TextField(db_column='ElectionType', blank=True)  # Field name made lowercase.
    electionyear = models.TextField(db_column='ElectionYear', blank=True)  # Field name made lowercase.
    rptpdbegdate = models.TextField(db_column='RptPdBegDate', blank=True, null=True)  # Field name made lowercase.
    rptpdenddate = models.DateField(db_column='RptPdEndDate', blank=True, null=True)  # Field name made lowercase.
    rptrcvddate = models.DateTimeField(db_column='RptRcvdDate', blank=True, null=True)  # Field name made lowercase.
    cmterefername = models.TextField(db_column='CmteReferName', blank=True)  # Field name made lowercase.
    cmtename = models.TextField(db_column='CmteName', blank=True)  # Field name made lowercase.
    statecmte = models.NullBooleanField(db_column='StateCmte')  # Field name made lowercase.
    stateid = models.IntegerField(db_column='StateID', blank=True, null=True)  # Field name made lowercase.
    localcmte = models.NullBooleanField(db_column='LocalCmte')  # Field name made lowercase.
    localid = models.IntegerField(db_column='LocalID', blank=True, null=True)  # Field name made lowercase.
    id = models.BigIntegerField(primary_key=True,unique=True)

    def __unicode__(self):
    	return '%s: %s, %s' % (self.amount, self.lastonlyname, self.rcvdate)

    class Meta:
        managed = False
        db_table = 'receipts'