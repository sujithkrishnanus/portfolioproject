from django.db import models

# Create your models here.

class personalDetails(models.Model):
    name= models.CharField(max_length=200)
    address= models.CharField(max_length=1000)
    mobile= models.IntegerField()
    email= models.CharField(max_length=200)
    profile = models.CharField(max_length=60)
    about_you= models.CharField(max_length=800)
    profile_photo=models.ImageField(upload_to='profile_photo')
    background_image = models.ImageField(upload_to='background_image')

    def __str__(self):
        return '{}'.format(self.name)

class education(models.Model):
    qualification= models.CharField(max_length=60)
    institution = models.CharField(max_length=50)
    duration_from= models.CharField(max_length=20)
    duration_to = models.CharField(max_length=20)
    about_qualification= models.CharField(max_length=300)

    def __str__(self):
        return '{}'.format(self.qualification)

class experience(models.Model):
    position= models.CharField(max_length=60)
    duration_from = models.CharField(max_length=20)
    duration_to = models.CharField(max_length=20)
    company_name = models.CharField(max_length=70)
    experience_summary = models.CharField(max_length=1000)

    def __str__(self):
        return '{}'.format(self.company_name)

class project(models.Model):
    project_name=models.CharField(max_length=100)
    project_description = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='project_image')
    link=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.project_name)

class socialMedia(models.Model):
    twitter= models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.instagram)

class skill(models.Model):
    skill=models.CharField(max_length=50)
    skill_rate=models.IntegerField()