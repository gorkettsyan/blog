from django.shortcuts import render
from django.views.generic import TemplateView
from writings.models import Writing
from django.contrib.auth.models import User
from django.http import HttpResponse





def homeview(request):
	template_name = 'home/home.html'
	context = {
	}
	return render(request, template_name, context)




def contactview(request):
	template_name = 'home/contact.html'
	context = {
	}
	return render(request, template_name, context)



def aboutview(request):
	template_name = 'home/about.html'
	context = {
	}
	return render(request, template_name, context)
