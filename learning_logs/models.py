from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """this is topic"""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """show topic's detail"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def jundestrnum(self):
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50]+'...'

    def __str__(self):
        return self.jundestrnum()

