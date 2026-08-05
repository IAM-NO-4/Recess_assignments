from django.shortcuts import (render,get_object_or_404,
redirect)
from django.http import HttpResponse
from .models import Student,Subject,Marks

def student_info(request,id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student": student
    }
    return render(request, "students/student_details.html",context)

def add_marks(request):
    if request.method == "POST":
        st_id = request.POST["student"]
        sbj_id = request.POST["subject"]
        marks = request.POST['score']
        Marks.objects.create(
            student = Student.objects.get(id=st_id),
            subject = Subject.objects.get(id= sbj_id),
            score= marks
        )
        return redirect("home")
    students = Student.objects.all()
    subjects = Subject.objects.all()
    context = {
        "students": students,
        "subjects" : subjects
    }
    return render(request, "students/add_marks.html", context)

def view_students(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request,"students/view_students.html", context)


def add_student(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        age = request.POST["age"]
        st_number = request.POST["st_number"]
        st_class = request.POST["st_class"]
        Student.objects.create(
            fname= fname,
            lname= lname,
            age= age,
            student_class= st_class,
            student_number= st_number
        )
        return redirect("home")
    return render(request, "students/add_student.html")

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        age = request.POST["age"]
        st_number = request.POST["st_number"]
        st_class = request.POST["st_class"]

        student.fname = fname 
        student.lname = lname
        student.student_class = st_class
        student.student_number = st_number
        student.age = age
        student.save()
        return redirect("view_students")
    context = {
        "student" : student
    }
    return render(request,"students/edit_student.html",context)

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("view_students")   

def wel(request):
    # kato = Student.objects.get(fname="kato")
    # kabejja = Student.objects.filter(fname= "kabejja").update(lname= "kawajji")
    students = Student.objects.all()
    # kato.marks = 34
    # kato.save()
    context = {
        "students": students
    }
    return render(request, "students/home.html ",context )