from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


   
# New story
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image=models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={'pk': self.pk})
    
    # Comments
class Comment(models.Model):
    post=models.ForeignKey(
        NewsStory,
        related_name="comments",
        on_delete=models.CASCADE,
    )
    author=models.ForeignKey(
        get_user_model(),
         on_delete=models.CASCADE
    )
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)

    