from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from social_auth.backends import get_backend
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
	if request.POST.get('choice')=="1":
		details.vote_1=details.vote_1+1
		

	if request.POST.get('choice')=="2":
		details.vote_2=details.vote_2+1
	if request.POST.get('choice')=="3":
		details.vote_3=details.vote_3+1
	if request.POST.get('choice')=="4":
		details.vote_4=details.vote_4+1

	details.response=details.response+1
	c=request.POST.get('choice')
	details.save()
	reason=request.POST.get('reason')

	return render(request,'urpoll/details.html',{'details':details,'reason':reason})

def reason_opt(request,id):
		ques=Question.objects.get(pk=id)
		ans1=request.POST.get('ans')
		ctext=request.POST.get('test')
		if ctext:
			if ans1=="1":
				c=comment_A(question=ques,userid="1",text=ctext)
				c.save()
			elif ans1=="2":
				c=comment_B(question=ques,userid="2",text=ctext)
				c.save()
			elif ans1=="3":
				c=comment_C(question=ques,userid="3",text=ctext)
				c.save()
			elif ans1=="4":
				c=comment_D(question=ques,userid="4",text=ctext)
				c.save()

		return render(request,'urpoll/details.html',{})

def get_comments_A(request,id):
	c=comment_A.objects.filter(question=id)
	return render(request,'urpoll/blank.html',{'comments':c})

def get_comments_B(request,id):
	c=comment_B.objects.filter(question=id)
	return render(request,'urpoll/blank.html',{'comments':c})

def get_comments_C(request,id):
	c=comment_C.objects.filter(question=id)
	return render(request,'urpoll/blank.html',{'comments':c})

def get_comments_D(request,id):
	c=comment_D.objects.filter(question=id)
	return render(request,'urpoll/blank.html',{'comments':c})


