from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'emp_name', 'designation', 'created_at', 'updated_at']
    search_fields = ['emp_id', 'emp_name', 'designation']
    list_filter = ['designation']

admin.site.register(Employee, EmployeeAdmin)
