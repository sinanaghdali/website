from django.contrib import admin
from mysite.models import Contact,newsletter

# Register your models here.
class Contactadmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ['title','author','status','publish_date','created_date']
    list_filter = ['status', 'author']
 
 
admin.site.register(Contact)
admin.site.register(newsletter) 