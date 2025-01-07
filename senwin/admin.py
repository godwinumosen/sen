from django.contrib import admin
# Register your models here.
from . import models
from .models import SenwinMainPost,SenwinProjectPost,Contactvideo,SenwinLatestPost

#The Senwin main post model admin
class SenwinMainPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'senwin_slug': ('senwin_title',)}
    list_display = ['senwin_title','senwin_description','senwin_author','senwin_slug']
admin.site.register(SenwinMainPost, SenwinMainPostModelAdmin)

class SenwinLatestPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'latest_post_slug': ('latest_post_title',)}
    list_display = ['latest_post_title','latest_post_description','latest_post_slug']
admin.site.register(SenwinLatestPost, SenwinLatestPostModelAdmin)

#The Senwin Project Post main post model admin
class SenwinProjectPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'senwin_project_slug': ('senwin_project_title',)}
    list_display = ['senwin_project_title','senwin_project_description','senwin_project_author','senwin_project_slug']
admin.site.register(SenwinProjectPost, SenwinProjectPostModelAdmin)

class ContactvideoModelAdmin (admin.ModelAdmin):
    list_display = ['contact_video']
admin.site.register(Contactvideo, ContactvideoModelAdmin)