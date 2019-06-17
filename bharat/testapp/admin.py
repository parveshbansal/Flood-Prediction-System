from django.contrib import admin
from testapp.models import User
class StudentAdmin(admin.ModelAdmin):
	list_display=['name','phoneno','village']
admin.site.register(User,StudentAdmin)	
