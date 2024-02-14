from django.db import models
from django.utils import timezone
from catalog.models import Scape




class Entry(models.Model):
    scape = models.ForeignKey(Scape, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000)