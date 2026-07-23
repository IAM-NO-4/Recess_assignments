# from django.db import models as db

# class Marks(db.Model):
#     student = db.ForeignKey('students.Student', on_delete=db.CASCADE)
#     subject = db.CharField(max_length=100)
#     marks_obtained = db.FloatField(max_length=5)

#     def __str__(self):
#         return f"{self.student.fname} {self.student.lname} - {self.subject}: {self.marks_obtained}"