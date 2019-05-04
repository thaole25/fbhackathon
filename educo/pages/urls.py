from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('teacherhome', HomePageView.as_view(), name='studenthome'),
    path('studenthome', HomePageView.as_view(), name='teacherhome'),
]
