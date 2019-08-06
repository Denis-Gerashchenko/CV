from django.db import models

# Create your models here.


class ProjectDone(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    overview = models.TextField()
    technology_used = models.TextField()


class Experience(models.Model):
    vacancy = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    work_expirience = models.CharField(max_length=100)
