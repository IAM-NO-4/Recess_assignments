from django import forms as fm
from .models import Marks, Student

class MarkForm(fm.ModelForm):
    class Meta:
        model = Marks
        fields = ["student", "subject", "score"]
        labels = {
            "student" :"Student Name",
            "score": "Marks scored"
        }
        help_texts = {
            # "score": "Score should be between 0 and 100"
        }
        widgets = {
            "score": fm.NumberInput(
                attrs={
                    "placeholder":"enter student's marks",
                    "class": "form-control"
                }
            ),
            "subject": fm.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "student": fm.Select(
                 attrs={
                     "class": "form-control"
                }
            )
        }
    def clean(self):
        cleaned_data =  super().clean()
        subject = self.cleaned_data.get("subject")
        student = self.cleaned_data.get("student")

        if subject and student:
            existing_mark = Marks.objects.filter(
                student=student,
                subject=subject
            ).exclude(pk=self.instance.pk).exists()
            if existing_mark:
                raise fm.ValidationError(
                    "Duplicate entry"
                )
        return cleaned_data

class StudentForm(fm.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "fname": "First name",
            "lname" : "Last name",
            "student_class" : "Class"
        }
    def clean_fname(self):
        fname = self.cleaned_data["fname"]
        if not fname[0].isalpha():
            raise fm.ValidationError(
                "A name cannot start with a number"
            )
        return fname

    def clean_lname(self):
        lname = self.cleaned_data["lname"]
        if not lname[0].isalpha():
            raise fm.ValidationError(
                "A name cannot start with a number"
            )
        return lname
    def clean_student_class(self):
        st_class = self.cleaned_data["student_class"]
        if st_class[0].islower():
            raise fm.ValidationError(
                "Start with capital letters"
            )
        return st_class

    def clean(self):
        cleaned_data = super().clean()
        fname = cleaned_data.get("fname")
        lname = cleaned_data.get("lname")
        if fname and lname:
            if fname.lower() == lname.lower():
                raise fm.ValidationError(
                    "First name and last name cannot be the same."
                )
        return cleaned_data
        