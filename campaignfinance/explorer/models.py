from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=128, unique=True)
    ward = models.IntegerField(max_length=2, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Candidate(models.Model):
	races = models.ManyToManyField(Race)
    nameFirst = models.CharField(max_length=128, unique=True)
    nameLast = models.CharField(max_length=128, unique=True)
    incumbant = models.BooleanField(default=False)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return '%s %s' % (self.nameFirst, self.nameLast)

class Committee(models.Model):
	candidate = models.ForeignKey(Candidate)
	committeeid = models.IntegerField(max_length=6, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return '%s: %s' % (self.committeeid, self.candidate)