from django.urls import path

from .views import HomePageView, DashboardPageView, loginRedirect

urlpatterns = [
    path('', HomePageView, name='home'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
    path('$', loginRedirect, name='login_redirect')
]
