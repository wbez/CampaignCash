from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from explorer.models import Receipts,Race,AppCandidate,AppCommittee


def index(request):
	race_list = Race.objects.filter(ward__lt=6)
	context_dict = {'races': race_list}

	return render(request, 'explorer/index.html', context_dict)

def race(request, ward):
	race = get_object_or_404(Race,ward=ward)
	context_dict = {'race': race}

	return render(request, 'explorer/race.html', context_dict)

def candidate(request, id):
	candidate_obj = get_object_or_404(AppCandidate,id=id)
	context_dict = {'candidate': candidate_obj}
	context_dict['receipts'] = Receipts.objects.filter(committeeid__candidate__id = id)

	return render(request, 'explorer/detail.html', context_dict)