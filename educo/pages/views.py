from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from schools.models import School

# class HomePageView(TemplateView):
#     template_name = 'pages/home.html'

def HomePageView(request):
    schools = School.objects.all()
    return render(request, 'pages/home.html', {'schools':schools})

class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'

def loginRedirect(request):
    if request.user.groups.filter(name="teachers").exists():
        return redirect("teachers/dash")
    else:
        return redirect("student/dash")

