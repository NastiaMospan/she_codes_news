from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment


class StoryForm(ModelForm):
    class Meta:        
        model = NewsStory        
        fields = ['title', 'pub_date', 'content', 'image']
        widgets = {
            'pub_date': forms.DateTimeInput(
                format=['%d/%m/%Y %H:%M'], 
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'datetime-local'
                    }
                    ),
                    }

       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  

    def clean_text(self):
        text = self.cleaned_data['text']
       
        return text
 
