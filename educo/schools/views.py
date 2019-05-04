# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'schools/home.html'

class JoinPageView(TemplateView):
    template_name = 'schools/join.html'

class JoinSucceedPageView(TemplateView):
    template_name = 'schools/succeed.html'