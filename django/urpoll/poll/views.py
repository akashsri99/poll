from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from poll.models import category,Question,comment_A,comment_B,comment_C,comment_D

def index(request):
	categorys=category.objects.order_by('Name')
	ques=Question.objects.order_by('-date')
	return render(request,'urpoll/index.html',{'category':categorys,'ques':ques})

def cat(request,id):
	categorys=category.objects.order_by('Name')
	ques=Question.objects.filter(category=id)
	return render(request,'urpoll/index.html',{'ques':ques,'category':categorys})

def detail(request,id):
	categorys=category.objects.order_by('Name')
	details=Question.objects.get(pk=id)
	return render(request,'urpoll/details.html',{'details':details,'category':categorys})

def submit_form(request,id):
	details = get_object_or_404(Question, pk=id)
	if request.POST['choice']=="1":
		details.vote_1=details.vote_1+1
		comment=get_object_or_404(comment_A,pk=id)
		comment.text=request.POST['reason']

	if request.POST['choice']=="2":
		details.vote_2=details.vote_2+1
		comment=get_object_or_404(comment_B,pk=id)
		comment.text=request.POST['reason']
	if request.POST['choice']=="3":
		details.vote_3=details.vote_3+1
		comment=get_object_or_404(comment_C,pk=id)
		comment.text=request.POST['reason']
	if request.POST['choice']=="4":
		details.vote_4=details.vote_4+1
		comment=get_object_or_404(comment_D,pk=id)
		comment.text=request.POST['reason']

	comment.save()

	details.response=details.response+1
	c=request.POST['choice']
	details.save()
	reasons=request.POST['reason']

	return render(request,'urpoll/details.html',{'details':details,'reasons':reasons})
