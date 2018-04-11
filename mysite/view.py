#from django.http import HttpResponse

from django.shortcuts import render
import datetime

def hello(request):
	context  = {}
	context['hello'] = datetime.datetime.now()
	context['second'] = ['a', 'b', 'c', 'd']
	return render(request, 'hello.html', context)