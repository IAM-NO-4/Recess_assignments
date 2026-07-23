from django.db import models as db

class Student(db.Model):
    fname = db.CharField(max_length=100)
    lname = db.CharField(max_length=100)
    student_class = db.CharField(max_length=10)
    age = db.IntegerField(max_length=3)
    student_number = db.IntegerField(unique=True)
    marks = db.FloatField(max_length=5)

    def __str__(self):
        return f"{self.fname} {self.lname} (Student No: {self.student_number})"