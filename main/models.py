from django.db import models

# Create your models here.

 

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, default="ShotbyMistake.png")
    website_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)
    tags =  models.ManyToManyField(Tag, null=True)
     

    def __str__(self):
        return self.website_name

class Other_Post(models.Model):
    thumbnail = models.ImageField( null=True, blank=True, default="ShotbyMistake.png" )
    website_name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)
    tags =  models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.website_name


class Skill_Name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Skill(models.Model):
    skill = models.ManyToManyField(Skill_Name, null=True)

    def __str__(self):
        return self.skill



class About_Name(models.Model):
    description = models.TextField(default='SOME STRING')

    def __str__(self):
        return self.description

class About(models.Model):
    about = models.ManyToManyField(About_Name, null=True)

    def __str__(self):
        return self.about
