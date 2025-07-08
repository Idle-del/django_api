# from django.utils import timezone
from django.db import models

class Student(models.Model):
    
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=30)
    branch = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name
