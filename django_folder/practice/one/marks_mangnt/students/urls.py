from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test_user),
    path("", views.wel, name= "home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("student/add/", views.add_student, name="add_student"),
    path("view/",views.view_students, name="view_students"),
    path("marks/add/",views.add_marks, name="add_marks"),
    path("summary/", views.summary, name="summary"),
    path("marks/delete/<int:id>",views.delete_marks, name="delete_marks"),
    path("class/details/<str:clas>/", views.class_info, name="class_info"),
    path("marks/<int:id>/edit", views.edit_marks, name="edit_marks"),
    path("student/delete/<int:id>/", views.delete_student, name= "delete_student"),
    path("edit/<int:id>/",views.edit_student,name="edit_student"),
    path("student/<int:id>/", views.student_info, name="student_details"),
    
      ]