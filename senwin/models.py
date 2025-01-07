from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date

# The main model for my portfolio category
class SenwinMainPost(models.Model):
    senwin_title = models.CharField(max_length=255, blank=True, null=True)
    senwin_description = models.TextField()
    senwin_slug = models.SlugField (max_length=255,blank=True, null=True)
    senwin_image= models.ImageField(upload_to='images_sen/')
    senwin_publish_date = models.DateTimeField (auto_now_add= True)
    senwin_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-senwin_publish_date']
    
    def __str__(self):
        return self.senwin_title + ' | ' + str(self.senwin_author)
    
    def get_absolute_url(self):
        return reverse('home')
    
class SenwinProjectPost(models.Model):
    senwin_project_title = models.CharField(max_length=255, blank=True, null=True)
    senwin_project_description = models.TextField()
    senwin_project_slug = models.SlugField (max_length=255,blank=True, null=True)
    senwin_project_image= models.ImageField(upload_to='images_project/')
    senwin_project_publish_date = models.DateTimeField (auto_now_add= True)
    senwin_project_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-senwin_project_publish_date']
    def __str__(self):
        return self.senwin_project_title + ' | ' + str(self.senwin_project_author)
    
    def get_absolute_url(self):
        return reverse('home')
    
#The Contactvideo on deusmagnus website
class Contactvideo(models.Model):
    contact_video = models.FileField(upload_to='contact_videos/') 


class SenwinLatestPost(models.Model):
    latest_post_title = models.CharField(max_length=255, blank=True, null=True)
    latest_post_description = models.TextField()
    latest_post_slug = models.SlugField (max_length=255,blank=True, null=True)
    latest_post_image= models.ImageField(upload_to=' latest_post/')
    latest_post_publish_date = models.DateTimeField (auto_now_add= True)
    latest_post_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering =['-latest_post_publish_date']
    def __str__(self):
        return self. latest_post_title + ' | ' + str(self. latest_post_author)
    
    def get_absolute_url(self):
        return reverse('home')
    