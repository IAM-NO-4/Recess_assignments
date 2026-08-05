from django.urls import path
from . import views

urlpatterns = [
    path("", views.wel, name= "home"),
    path("student/add/", views.add_student, name="add_student"),
    path("view/",views.view_students, name="view_students"),
    path("marks/add/",views.add_marks, name="add_marks"),
    path("delete/<int:id>/", views.delete_student, name= "delete_student"),
    path("edit/<int:id>/",views.edit_student,name="edit_student"),
    path("student/<int:id>/", views.student_info, name="student_details"),
    
      ]