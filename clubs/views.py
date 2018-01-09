from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	
	return render(request, 'clubs/home.html')

def information(request):
	return render(request, 'clubs/information.html')

def locations(request):
	return render(request, 'clubs/locations.html')

def dubai(request):
	return render(request, 'clubs/dubai.html')

def albarshamixed(request):
	return render(request, 'clubs/albarshamixed.html')

def albarshamixedmembership(request):
	return render(request, 'clubs/albarshamixed_membership.html')

def albarshamixedoptions(request):
	return render(request, 'clubs/albarshamixed_options.html')


