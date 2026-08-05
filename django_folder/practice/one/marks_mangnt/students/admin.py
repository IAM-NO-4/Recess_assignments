from django.contrib import admin
from .models import Student
from .models import Marks
from .models import Subject

admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Subject)
