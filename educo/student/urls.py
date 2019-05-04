from django.urls import path
from .views import StudentView, StudentDashView

urlpatterns = [
    path('', StudentView.as_view(), name='student'),
    path('dash', StudentDashView.as_view(), name='studentdash'),
]