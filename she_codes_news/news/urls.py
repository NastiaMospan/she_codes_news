from django.urls import path,include
from . import views

# from .views import account_view

app_name = 'news'

urlpatterns = [
    
    path('story/', views.IndexView.as_view(), name='index'),
    path('author/<str:username>', views.AuthorDetailView.as_view(), name='authordetail'),
    path('story/<int:pk>/comment', views.AddCommentView.as_view(), name="addComment"),
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('story/add/', views.AddStoryView.as_view(), name='newStory'),
]
