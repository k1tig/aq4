from django.db import models
from django.utils import timezone
from catalog.models import Scape, Plant




class Entry(models.Model):
    scape = models.ForeignKey(Scape, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000)
    plant_tags = models.ManyToManyField(Plant, blank=True)