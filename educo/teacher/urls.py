from django.urls import path

from .views import TeacherView

urlpatterns = [
    path('teacherhome', TeacherView.as_view(), name='studenthome'),
]
