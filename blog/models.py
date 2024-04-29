from django.conf import settings
from django.db import models
from django.utils import timezone
from .utils import generate_slug
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Category, self).save(*args, **kwargs);
    
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)   
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Post, self).save(*args, **kwargs);



