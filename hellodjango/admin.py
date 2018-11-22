from django.contrib import admin

from .models import EmpNew,Student,Emp
# Register your models here.


class studentAdmin(admin.ModelAdmin):
    date_hierarchy = 'createDate'

    fieldsets = (
            ('基本信息', {
                'fields': ('name', 'sex')
            }),
            ('高级信息', {
                'classes': ('collapse',),
                'fields': ('addr','createDate'),
            }),
        )

    list_display = ('id','name', 'sex','addr','createDate')
    search_fields = ['id',]
    #list_editable = ('name','sex','addr',)
    readonly_fields = ('createDate',)
    list_per_page = 10



admin.site.register(Student,studentAdmin)


class empNewAdmin(admin.ModelAdmin):

    fields = ('emp_name','gender','mobile_phone')
    list_display = ('emp_id', 'emp_name', 'gender', 'mobile_phone')


admin.site.register(EmpNew,empNewAdmin)


class empAdmin(admin.ModelAdmin):
    fields = ('name','age' ,'sex','birthDay')
    list_display = ('id','name','age')

admin.site.register(Emp,empAdmin)
