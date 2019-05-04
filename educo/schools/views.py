from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'schools/home.html'

class JoinPageView(TemplateView):
    template_name = 'schools/join.html'

class JoinSubmitPage(TemplateView):
    template_name = 'schools/submit.html'