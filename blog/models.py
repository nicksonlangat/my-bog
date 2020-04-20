from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
    	return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image   =   models.ImageField(upload_to="post/%Y/%m/%d", blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    slug        =   models.SlugField(max_length=140, blank=True, unique=True, null=True)
    def __str__(self):
    	return self.title
    def get_absolute_url(self):
    	return reverse('blog_detail', args=[str(self.slug)])
    class Meta:
        ordering=('-created_on', )
def slug_generator(sender, instance, *args, **kargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=Post)