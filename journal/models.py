from django.db import models
from django.utils import timezone
from catalog.models import Scape
from django.forms import ModelForm, forms
from django.contrib.auth.models import User



class Entry(models.Model):
    scape = models.ForeignKey(Scape, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000)