from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

app_name = 'blog'

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CATEGORY_CHOICES = (
        ('maktabga', 'Maktabga oid'),
        ('talimga', 'Ta\'limga oid'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, default='blog/no_image.png')
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default='maktabga')
    views = models.IntegerField(default=0, verbose_name='Views')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month,
        											self.publish.day, self.slug])