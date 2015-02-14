from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from poll.models import category,Question,comment_A

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
	ctext=request.POST.get('test')
	C=comment_A(question=details,userid="1",text=ctext)
	C.save()
	if request.POST['choice']=="1":
		details.vote_1=details.vote_1+1
		

	if request.POST['choice']=="2":
		details.vote_2=details.vote_2+1
	if request.POST['choice']=="3":
		details.vote_3=details.vote_3+1
	if request.POST['choice']=="4":
		details.vote_4=details.vote_4+1

	details.response=details.response+1
	c=request.POST['choice']
	details.save()
	reason=request.POST['reason']

	return render(request,'urpoll/details.html',{'details':details,'reason':reason})

def testsave(request,id):
	request.POST['test']
	ctext=request.POST['test']
	Q=Question.objects.get(pk=id)
	C=comment_A(question=Q,userid="1",text=ctext)
	C.save()
	return render(request,'urpoll/details.html',{})

