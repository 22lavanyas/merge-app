from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin
from .utils import generate_slug
import uuid

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    def str(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now  
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.question_text);
        super(Question, self).save(*args, **kwargs)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    choice_slug = models.SlugField(unique=True, default=uuid.uuid1)

    def str(self):
        return self.choice_text
    
    def save(self, *args, **kwargs):
        if not self.question:
            raise ValueError("Question field must be set before saving Choice instance.")
        self.choice_slug = generate_slug(self.choice_text)
        super().save(*args, **kwargs)