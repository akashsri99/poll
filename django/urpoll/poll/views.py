from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import RequestContext,loader
from poll.models import category,Question,comment_A,comment_B,comment_C,comment_D,votes_ques
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	try:
		details=Question.objects.get(pk=id)
		related=Question.objects.filter(category=details.category.id)
	except Question.DoesNotExist:
		return render(request,'urpoll/404.html',{'category':categorys})

	return render(request,'urpoll/details.html',{'details':details,'category':categorys,'related':related})

def submit_form(request,id):
	details = get_object_or_404(Question, pk=id)
	related=Question.objects.filter(category=details.category)
	
	if request.POST.get('choice')=="1":
		details.vote_1=details.vote_1+1

		audit=votes_ques(person_id=request.POST.get('userid'),quesid=details.id,ans_id=1)
		

	if request.POST.get('choice')=="2":
		details.vote_2=details.vote_2+1
		audit=votes_ques(person_id=request.POST.get('userid'),quesid=details.id,ans_id=2)
		
	if request.POST.get('choice')=="3":
		details.vote_3=details.vote_3+1
		audit=votes_ques(person_id=request.POST.get('userid'),quesid=details.id,ans_id=3)
		
	if request.POST.get('choice')=="4":
		details.vote_4=details.vote_4+1
		audit=votes_ques(person_id=request.POST.get('userid'),quesid=details.id,ans_id=4)
		

	details.response=details.response+1
	c=request.POST.get('choice')
	details.save()
	audit.save()
	reason=request.POST.get('reason')

	return render(request,'urpoll/details.html',{'details':details,'related':related})

def reason_opt(request,id):
		ques=Question.objects.get(pk=id)
		ans1=request.POST.get('ans')
		ctext=request.POST.get('test')
		user=request.POST.get('username1')
		if ctext:
			if ans1=="1":
				c=comment_A(question=ques,userid=user,text=ctext)
				c.save()
			elif ans1=="2":
				c=comment_B(question=ques,userid=user,text=ctext)
				c.save()
			elif ans1=="3":
				c=comment_C(question=ques,userid=user,text=ctext)
				c.save()
			elif ans1=="4":
				c=comment_D(question=ques,userid=user,text=ctext)
				c.save()

		return render(request,'urpoll/blank.html',{})

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


def submit_question(request,id):
	c=category.objects.get(Name=request.POST.get('Category'))
	q=Question(category=c,question=request.POST.get('question'),date=datetime.datetime.now(),option1=request.POST.get('opA'),option2=request.POST.get('opB'),option3=request.POST.get('opC'),option4=request.POST.get('opD'))
	q.save()
	categorys=category.objects.order_by('Name')
	ques=Question.objects.order_by('-date')
	return render(request,'urpoll/index.html',{'category':categorys,'ques':ques})

