from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class StudentView(TemplateView):
    template_name = 'student/student.html'

class StudentDashView(TemplateView):
    template_name = 'student/dash.html'