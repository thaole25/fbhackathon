from django.shortcuts import render
from django.views.generic import TemplateView


class TeacherView(TemplateView):
    template_name = 'teacher/teacher.html'

class MaterialMarketView(TemplateView):
    template_name = 'teacher/tutemarket.html'

class MaterialContentView(TemplateView):
    template_name = 'teacher/materialcontent.html'

class FilteredMaterialContentView(TemplateView):
    template_name = 'teacher/tutemarket1.html'

class TeacherDashView(TemplateView):
    template_name = 'teacher/dash.html'

class TeacherAnalysisManageView(TemplateView):
    template_name = 'teacher/analysis_manage.html'

