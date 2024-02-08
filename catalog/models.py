from django.db import models

from django.contrib.auth.models import User 



class Profile(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "user")
    country = models.CharField(max_length=200, blank = True)
    instagram = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name.username

class Plant(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Fish(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Fish"

    def __str__(self):
        return self.name
    
class Invertebrate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class TankSize(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
class TankVolume(models.Model):
    volume = models.CharField(max_length=10)

    def __str__(self):
        return self.volume

class TankFilter(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TankLight(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TankCo2(models.Model):
    co2 = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = "Co2"
    
    def __str__(self):
        return self.co2
    
class TankSoil(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TankHardscape(models.Model):
    HARDSCAPE_TYPES=[
        ("s" , "Stone"),
        ("w" , "Wood"),
    ]

    name = models.CharField(max_length=100)
    hardscape_type = models.CharField(choices = HARDSCAPE_TYPES, max_length=10)

    def __str__(self):
        return self.name


#Users Scape Data
class Scape(models.Model):
    scape_name = models.CharField(max_length=100)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = "owner_name")
    size = models.ForeignKey(TankSize, on_delete=models.CASCADE)
    volume = models.ForeignKey(TankVolume, on_delete=models.CASCADE)
    filtration = models.ForeignKey(TankFilter, on_delete=models.CASCADE)
    lighting = models.ForeignKey(TankLight, on_delete=models.CASCADE)
    co2 = models.ForeignKey(TankCo2, on_delete=models.CASCADE)
    soil = models.ForeignKey(TankSoil, on_delete=models.CASCADE)

    hardscape = models.ManyToManyField(TankHardscape, blank = True)
    fish = models.ManyToManyField(Fish, blank = True)
    invertebrate = models.ManyToManyField(Invertebrate, blank = True)

    plants = models.ManyToManyField(Plant, related_name= "fucking_scape_id", blank = True)

    def __str__(self):
        return self.scape_name




