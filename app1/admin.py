from django.contrib import admin
from .models import Employe,AddressDetails,WorkExperience,Qualifications,Projects

# Register your models here.
# admin.site.register(Student)

# class Address_config(admin.TabularInline):
#     model = AddressDetails



class Employe_add(admin.ModelAdmin):
    # inlines = [Address_config]
    list_display = ['id','name','email','addressDetails','workExperience','qualifications',
                    'projects','photo']


admin.site.register(Employe,Employe_add)
admin.site.register(AddressDetails)
admin.site.register(WorkExperience)
admin.site.register(Qualifications)
admin.site.register(Projects)

