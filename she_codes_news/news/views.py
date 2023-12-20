from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory 
from .forms import StoryForm, CommentForm
from django.shortcuts import render
from users.models import CustomUser
from django.shortcuts import redirect, get_object_or_404
from django import forms
from .models import Comment




class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"
    
    def get_queryset(self):
        filter_to_author = self.request.GET.get('author', None)
        qs = NewsStory.objects.all()
        if filter_to_author:
           qs = NewsStory.objects.filter(
            author__username=filter_to_author
        )   
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by("-pub_date")[:4]
        context['users']=CustomUser.objects.order_by("username")
        context['filter_to_author'] = self.request.GET.get('author', None)
        return context

class StoryView(generic.DetailView):
     model = NewsStory
     template_name = 'news/story.html'
     context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



    # adding filter by author
class AuthorDetailView(generic.DetailView):
     model=CustomUser
     template_name='news/index.html'
     context_object_name="author"

     def get_object(self, *args, **kwargs):
         return get_object_or_404(CustomUser, 
         username=self.kwargs['username'])
     
     def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         selected_author = self.request.GET.get('author') 
         if selected_author:
            # Filter by selected author if one is chosen
            context['all_stories'] = NewsStory.objects.filter(author__username=selected_author)
         else:
            # If no author selected, display all stories
            context['all_stories'] = NewsStory.objects.filter(author_id=self.object.id)
        
         return context
     
# adding comments
class AddCommentView(generic.CreateView):
    form_class = CommentForm  
    template_name='news/Index.html'

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk': self.kwargs.get("pk")})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()  
        return context





