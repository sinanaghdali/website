from django.contrib import admin
from blog.models import post,category

# Register your models here.

class postadmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ['title','author','status','publish_date','created_date']
    list_filter = ['status', 'author']
 
admin.site.register(category)
admin.site.register(post,postadmin)