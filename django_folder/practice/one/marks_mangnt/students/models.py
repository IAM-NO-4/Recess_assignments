from django.db import models as db
from django.core.validators import(MinValueValidator, MaxValueValidator)

class Student(db.Model):
    fname = db.CharField(max_length=100)
    lname = db.CharField(max_length=100)
    student_class = db.CharField(max_length=10)
    age = db.IntegerField(max_length=3)
    student_number = db.IntegerField(unique=True)

    def __str__(self):
        return f"{self.fname} {self.lname} (Student No: {self.student_number})"

class Subject(db.Model):
    name = db.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"

class Marks(db.Model):
    student = db.ForeignKey(Student, on_delete= db.CASCADE, related_name= "marks")
    subject = db.ForeignKey(Subject, on_delete=db.CASCADE,related_name= "marks")
    score = db.FloatField(max_length= 10,
                          validators=[
                              MinValueValidator(0),
                              MaxValueValidator(100)
                          ])
    class Meta:
        constraints = [
            db.UniqueConstraint(
                fields=["student", "subject"],
                name="unique_st_sub_mark"
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.subject}- {self.score}"
     
