from django.db import models

# Create your models here.
class category(models.Model):
	Name=models.CharField(max_length=20)

	def __unicode__(self):
		return self.Name

class Question(models.Model):
	category=models.ForeignKey(category)
	question=models.CharField(max_length=200)
	date=models.DateTimeField('date published')
	response=models.IntegerField(default=0)
	option1=models.CharField(max_length=50)
        option2=models.CharField(max_length=50)
	option3=models.CharField(max_length=50)
        option4=models.CharField(max_length=50)
	vote_1=models.IntegerField(default=0)
	vote_2=models.IntegerField(default=0)
	vote_3=models.IntegerField(default=0)
	vote_4=models.IntegerField(default=0)

	def __unicode__(self):
		return self.question

class option_2(models.Model):
	ques=models.ForeignKey(Question)
	option1=models.CharField(max_length=50)
	option2=models.CharField(max_length=50)
	vote_1=models.IntegerField(default=0)
	vote_2=models.IntegerField(default=0)

	def __unicode__(self):
		return self.ques

class option_4(models.Model):
	ques=models.ForeignKey(Question)
	option1=models.CharField(max_length=50)
        option2=models.CharField(max_length=50)
	option3=models.CharField(max_length=50)
        option4=models.CharField(max_length=50)
	vote_1=models.IntegerField(default=0)
	vote_2=models.IntegerField(default=0)
	vote_3=models.IntegerField(default=0)
	vote_4=models.IntegerField(default=0)

	def __unicode__(self):
		return self.id

class votes_ques(models.Model):
	person_id=models.CharField(max_length=200)
	quesid=models.IntegerField(default=0)
	ans_id=models.IntegerField(default=0)

