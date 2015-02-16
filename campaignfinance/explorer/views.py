from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from explorer.models import Receipts,Race,AppCandidate,AppCommittee
import json, datetime
from django.contrib.humanize.templatetags.humanize import intcomma


def index(request):
	race_list = Race.objects.filter(ward__gt=0)
	mayor = Race.objects.get(ward=0)
	context_dict = {'races': race_list,'mayor': mayor}

	return render(request, 'explorer/index.html', context_dict)

def race(request, slug):
	race = get_object_or_404(Race,slug=slug)
	context_dict = {'race': race}

	return render(request, 'explorer/race.html', context_dict)

def candidate(request, slug):
	candidate_obj = get_object_or_404(AppCandidate,slug=slug)
	context_dict = {'candidate': candidate_obj}
	context_dict['receipts'] = Receipts.objects.filter(committeeid__candidate__slug = slug)

	return render(request, 'explorer/detail.html', context_dict)

def datatables(request, slug):
	receipts = Receipts.objects.filter(committeeid__candidate__slug = slug)
	rows = []
	for receipt in receipts:
		amount = '$'+intcomma("{0:.2f}".format(receipt.amount))
		date = '{dt:%b}. {dt.day}, {dt.year}'.format(dt=receipt.rcvdate)
		row = [receipt.firstname,receipt.lastonlyname,amount,date,receipt.occupation,receipt.employer,receipt.city,receipt.state]
		rows.append(row)
	data = {'data':rows}
	return HttpResponse(json.dumps(data), content_type="application/json") 