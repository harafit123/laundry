from django.contrib import admin
from  .models import Enquiry,Profile
# Register your models here.

class  EnquiryAdmin(admin.ModelAdmin) :
	list_display=['name','email','message','is_resolved']
	list_filter=('contacted_date','is_resolved')
	list_editable=('is_resolved',)



admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Profile)