from django.shortcuts import (render,get_object_or_404,
redirect)
from django.db.models import Q, Max, Min, Avg, Sum,Count
from matplotlib.style import context
from .models import Student,Marks
from django.http import HttpResponse
from .forms import MarkForm, StudentForm
from django .core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login, logout, authenticate

@login_required
@permission_required('students.view_student', raise_exception=True)
def student_info(request,id):
    student = get_object_or_404(Student, id=id)
    marks = student.marks.all()
    results = marks.aggregate(
        average= Avg("score"),
        total= Sum("score"),
        highest= Max("score") ,
        smallest= Min("score"),
        subjects= Count("id")
    )
    context = {
        "student": student,
        "results" : results
    }
    return render(request, "students/student_details.html",context)

@login_required
@permission_required('students.change_marks', raise_exception=True)
def edit_marks(request,id):
    mark = get_object_or_404(Marks, id=id)
    if request.method == "POST":
        form = MarkForm(
            request.POST,
            instance=mark
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Marks eddited successfully")
            return redirect("student_details", id= mark.student.id)
    else:
        form = MarkForm(instance=mark)
        context = {
            "form" : form,
            "mark" : mark
        }
        return render(request, "students/edit_marks.html", context)

@login_required
@permission_required('students.add_marks', raise_exception=True)
def add_marks(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marks added successfully")
            return redirect("view_students")
    else:
        form = MarkForm()
    context = {
        'form': form
    }    
    return render(request, "students/add_marks.html", context)

def view_students(request):
    students = Student.objects.all()
    classes = Student.objects.values_list(
        "student_class",
        flat=True,
    
    ).distinct()
    search = request.GET.get("search")
    st_class = request.GET.get("class")
    if search or st_class:
        if search:
            students = Student.objects.filter(Q(fname__icontains=search)|
                                            Q(lname__icontains=search))
        if st_class:
            students = students.filter(student_class=st_class)    
    paginator = Paginator(students, 4)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)    
    
    context = {
                "students" : page_obj,
                "classes": classes,
                "page_obj" : page_obj
            }   
    return render(request,"students/view_students.html", context)

@login_required
@permission_required('students.add_student', raise_exception=True)
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect("view_students")
            

    else:
        form = StudentForm()
    context = {
        "form": form
     }
    return render(request,"students/add_student.html", context)
        
@login_required
@permission_required('students.delete_marks', raise_exception=True)
def delete_marks(request,id):
    mark = get_object_or_404(Marks , id=id)
    if request.method == "POST":
        student_id = mark.student.id
        mark.delete()
        messages.success(request, "Mark deleted successfully")
        return redirect("student_details", student_id)
    context = {
        "mark" : mark
    }
    return render(request, "students/delete_marks.html", context)

@login_required
@permission_required('students.change_student', raise_exception=True)
def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student eddited successfully")
            return redirect("view_students")
    else:
        form = StudentForm(instance=student)
    context = {
        "form" : form,
        "student": student
    }
    return render(request,"students/edit_student.html",context)

@login_required
@permission_required('students.delete_student', raise_exception=True)
def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect("view_students")   
    else:
        context = {
            "student": student
        }
        return render(request,"students/delete_student.html", context)


def wel(request):
    return render(request, "students/home.html " )

def class_info(request, clas):
    students = Student.objects.filter(student_class=clas)
    students = students.annotate(
        total=Sum("marks__score"),
        average=Avg("marks__score"),
        subjects=Count("marks__id")

    ).order_by("-average")
    paginator = Paginator(students, 2)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)

    context = {
        "students": page_obj,
        "class": clas,
        "page_obj": page_obj
    }
    return render(request, "students/class_info.html", context)

def summary(request):
    classes = Student.objects.values_list(
        "student_class",
        flat=True,
    ).distinct()
    context = {
        "classes": classes
    }
    return render(request, "students/summary_info.html", context)

def test_user(request):
    if request.user.is_authenticated:
         print(request.user)
    else:
        print("no user logged in")
    return HttpResponse("hello")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
             login(request, user)
             return redirect("view_students")
        else:
            context = {
                "error" : "invalid username or password"
            }
            return render(request, "students/login.html", context)
    return render(request, "students/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")