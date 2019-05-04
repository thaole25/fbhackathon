from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class TeacherView(TemplateView):
    template_name = 'pages/teacher.html'


class StudentView(TemplateView):
    template_name = 'pages/student.html'
