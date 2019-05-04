from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('join/', views.JoinPageView.as_view(), name='join'),
    path('submit/', views.JoinSubmitPage.as_view(), name='submit'),
]
