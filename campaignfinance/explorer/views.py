from django.shortcuts import render
from django.http import HttpResponse
from explorer.models import Receipts,Race,AppCandidate,AppCommittee


def index(request):
	race_list = Race.objects.all()
	context_dict = {'races': race_list}

	return render(request, 'explorer/index.html', context_dict)