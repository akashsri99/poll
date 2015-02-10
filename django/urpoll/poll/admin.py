from django.contrib import admin
from poll.models import category,Question,option_2,option_4,votes_ques
# Register your models here.
class option2Inline(admin.TabularInline):
	model=option_2

class option4Inline(admin.TabularInline):
	model=option_4

class QuesAdmin(admin.ModelAdmin):
	fieldsets=[]
	inlines=[option2Inline,option4Inline]

admin.site.register(category)
admin.site.register(Question,QuesAdmin)
