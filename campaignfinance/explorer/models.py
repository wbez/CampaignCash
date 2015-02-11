from django.db import models
from django.db.models import Sum
from django.utils.text import slugify

class Race(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ward = models.IntegerField(max_length=2, unique=True)
    slug = models.SlugField()
    description = models.TextField(blank=True)

    def get_absolute_url(self):
    	from django.core.urlresolvers import reverse
    	return reverse('explorer.views.race', args=[str(self.slug),str(self.id)])

    def save(self, *args, **kwargs):
    	self.slug = slugify(unicode(self.name))
    	super(Race, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class AppCandidate(models.Model):
	races = models.ManyToManyField(Race)
	nameFirst = models.CharField(max_length=128)
	nameLast = models.CharField(max_length=128)
	nameMiddle = models.CharField(max_length=128, blank=True)
	incumbant = models.BooleanField(default=False)
	slug = models.SlugField()
	bio = models.TextField(blank=True)

	def save(self, *args, **kwargs):
		slugvalue = '%s %s' % (self.nameFirst, self.nameLast)
		self.slug = slugify(unicode(slugvalue))
		super(AppCandidate, self).save(*args, **kwargs)

	def _get_all_contributions(self):
		"Returns the sum of contributions for this candidate"
		total = Receipts.objects.filter(committeeid__candidate=self.id).aggregate(Sum('amount'))
		return total['amount__sum']
	
	sum_contributions = property(_get_all_contributions)

	def __unicode__(self):
		return '%s %s' % (self.nameFirst, self.nameLast)

class AppCommittee(models.Model):
	committeeid = models.IntegerField(primary_key=True)
	name = models.TextField(max_length=255)
	candidate = models.ForeignKey(AppCandidate, null=True)
	slug = models.SlugField(max_length=255)

	def save(self, *args, **kwargs):
		self.slug = slugify(unicode(self.name))
		super(AppCommittee, self).save(*args, **kwargs)

	def _get_all_contributions(self):
		"Returns the sum of contributions for this committee"
		total = self.receipts_set.aggregate(Sum('amount'))
		return total['amount__sum']
	sum_contributions = property(_get_all_contributions)

	def __unicode__(self):
		return '%s: %s' % (self.committeeid, self.candidate)

class Receipts(models.Model):
    committeeid = models.ForeignKey(AppCommittee,db_column='CommitteeID')  
    lastonlyname = models.TextField(db_column='LastOnlyName', blank=True)  
    firstname = models.TextField(db_column='FirstName', blank=True)  
    rcvdate = models.DateField(db_column='RcvDate', blank=True, null=True)  
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  
    loanamount = models.FloatField(db_column='LoanAmount', blank=True, null=True)  
    occupation = models.TextField(db_column='Occupation', blank=True)  
    employer = models.TextField(db_column='Employer', blank=True)  
    address1 = models.TextField(db_column='Address1', blank=True)  
    address2 = models.TextField(db_column='Address2', blank=True)  
    city = models.TextField(db_column='City', blank=True)  
    state = models.TextField(db_column='State', blank=True)  
    zip = models.TextField(db_column='Zip', blank=True)  
    rcttype = models.TextField(db_column='RctType', blank=True)  
    description = models.TextField(db_column='Description', blank=True)  
    vendorlastonlyname = models.TextField(db_column='VendorLastOnlyName', blank=True)  
    vendorfirstname = models.TextField(db_column='VendorFirstName', blank=True)  
    vendoraddress1 = models.TextField(db_column='VendorAddress1', blank=True)  
    vendoraddress2 = models.TextField(db_column='VendorAddress2', blank=True)  
    vendorcity = models.TextField(db_column='VendorCity', blank=True)  
    vendorstate = models.TextField(db_column='VendorState', blank=True)  
    vendorzip = models.TextField(db_column='VendorZip', blank=True)  
    rpttype = models.TextField(db_column='RptType', blank=True)  
    electiontype = models.TextField(db_column='ElectionType', blank=True)  
    electionyear = models.TextField(db_column='ElectionYear', blank=True)  
    rptpdbegdate = models.TextField(db_column='RptPdBegDate', blank=True, null=True)  
    rptpdenddate = models.DateField(db_column='RptPdEndDate', blank=True, null=True)  
    rptrcvddate = models.DateTimeField(db_column='RptRcvdDate', blank=True, null=True)  
    cmterefername = models.TextField(db_column='CmteReferName', blank=True)  
    cmtename = models.TextField(db_column='CmteName', blank=True)  
    statecmte = models.NullBooleanField(db_column='StateCmte')  
    stateid = models.IntegerField(db_column='StateID', blank=True, null=True)  
    localcmte = models.NullBooleanField(db_column='LocalCmte')  
    localid = models.IntegerField(db_column='LocalID', blank=True, null=True)  
    id = models.BigIntegerField(primary_key=True,unique=True)

    def __unicode__(self):
    	return '%s: %s, %s' % (self.amount, self.lastonlyname, self.rcvdate)

    class Meta:
        managed = False
        db_table = 'receipts'

class Committees(models.Model):
    cmterefername = models.TextField(db_column='CmteReferName', blank=True)  
    statecmte = models.NullBooleanField(db_column='StateCmte')  
    stateid = models.IntegerField(db_column='StateID', blank=True, null=True)  
    localcmte = models.NullBooleanField(db_column='LocalCmte')  
    localid = models.IntegerField(db_column='LocalID', blank=True, null=True)  
    cmtename = models.TextField(db_column='CmteName', blank=True)  
    address1 = models.TextField(db_column='Address1', blank=True)  
    address2 = models.TextField(db_column='Address2', blank=True)  
    address3 = models.TextField(db_column='Address3', blank=True)  
    city = models.TextField(db_column='City', blank=True)  
    state = models.TextField(db_column='State', blank=True)  
    zip = models.TextField(db_column='Zip', blank=True)  
    status = models.TextField(db_column='Status', blank=True)  
    statusdate = models.DateField(db_column='StatusDate', blank=True, null=True)  
    typeofcommittee = models.TextField(db_column='TypeOfCommittee', blank=True)  

    class Meta:
        managed = False
        db_table = 'committees'