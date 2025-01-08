from django.contrib import admin
# Register your models here.
from . import models
from .models import SenwinMainPost,SenwinProjectPost,Contactvideo,SenwinLatestPost
from .models import CategoryPost,SecondCategoryPost

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

#The Catigory post model admin
class CategoryPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_title',)}
    list_display = ['category_title','category_description','category_slug']
admin.site.register(CategoryPost, CategoryPostModelAdmin)

#The second Catigory post model admin
class SecondCategoryPostModelAdmin (admin.ModelAdmin):
    prepopulated_fields = {'second_category_slug': ('second_category_title',)}
    list_display = ['second_category_title','second_category_description','second_category_slug']
admin.site.register(SecondCategoryPost, SecondCategoryPostModelAdmin)