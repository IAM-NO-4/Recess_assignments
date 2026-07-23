from django.shortcuts import render

def home(request):
    content = {
        "title": "Welcome to Student Marks Management System",
        "message": "This system allows you to manage student marks efficiently."
        }
    context = {
        "content": content
    }

    return render(request, "marks/home.html", context)

# Create your views here.
