from django.contrib import admin
from news.models import Comment, NewsStory

# Register your models here.


admin.site.register(Comment)
admin.site.register(NewsStory)