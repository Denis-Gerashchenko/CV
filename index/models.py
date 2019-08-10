from django.db import models

# Create your models here.


class ProjectDone(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    overview = models.TextField()
    technology_used = models.TextField()
    featured = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.TextField(max_length=100, null=True, blank=True)
    github = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    vacancy = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    work_experience = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    job_done = models.BooleanField()

    def __str__(self):
        return self.vacancy


class ProfilePhoto(models.Model):
    profile_photo = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    actual = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.actual)
