from django.urls import path

from .views import HomePageView, AboutPageView, TeacherView, StudentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('teacherhome/', TeacherView.as_view(), name='teacherhome'),
    path('studenthome/', StudentView.as_view(), name='studenthome'),
]
