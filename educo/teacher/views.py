from django.shortcuts import render
from django.views.generic import TemplateView


class TeacherView(TemplateView):
    template_name = 'teacher/teacher.html'


