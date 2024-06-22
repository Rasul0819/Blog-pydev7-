from django.contrib import admin
from .import models



class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','created','updated']
    list_display_links=['title','id']
admin.site.register(models.Blog,BlogAdmin)