from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from poll.models import category,Question

def index(request):
	categorys=category.objects.order_by('Name')
	return render(request,'urpoll/index.html',{'category':categorys})

def cat(request,id):
	ques=Question.objects.filter(category=id)
	return render(request,'urpoll/index.html',{'ques':ques})

def options(request,id):
	option=option_4.objects.filter(question=id)
	return render(request,'urpoll/index.html',{'option':option})