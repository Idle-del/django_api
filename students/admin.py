from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','branch', 'created_at', 'updated_at')
    search_fields = ('student_id', 'student_name', 'branch')
    list_filter = ('branch',)

admin.site.register(Student, StudentAdmin)