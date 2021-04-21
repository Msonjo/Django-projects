from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("My first django app. It will get better. Kudos at the ZURI team for making this possible.")

# Create your views here.
