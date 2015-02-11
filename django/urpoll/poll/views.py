from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from poll.models import category,Question

def index(request):
	categorys=category.objects.order_by('Name')
	return render(request,'urpoll/index.html',{'category':categorys})

def cat(request,id):
	categorys=category.objects.order_by('Name')
	ques=Question.objects.filter(category=id)
	return render(request,'urpoll/index.html',{'ques':ques,'category':categorys})

def detail(request,id):
	details=Question.objects.get(pk=id)
	return render(request,'urpoll/details.html',{'details':details})

def submit_form(request,id):
	details = get_object_or_404(Question, pk=id)
	if request.POST['choice']==1:
		details.vote=details.vote_1+1

	if request.POST['choice']==2:
		details.vote_2=details.vote_2+1
	if request.POST['choice']==3:
		details.vote_3=details.vote_3+1
	if request.POST['choice']==4:
		details.vote_4=details.vote_4+1
	c=request.POST['choice']

	return render(request,'urpoll/details.html',{'details':details,'test':c})
