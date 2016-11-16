from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer1_text = models.TextField(default="")
    answer2_text = models.TextField(default="")
    answer3_text = models.TextField(default="")
    answer4_text = models.TextField(default="")
    correct = models.IntegerField(default=1)