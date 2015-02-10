from django.contrib import admin
from poll.models import category,Question,votes_ques
# Register your models here.
admin.site.register(category)
admin.site.register(Question)
