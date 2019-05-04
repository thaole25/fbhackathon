from django.urls import path

from .views import TeacherView, MaterialMarketView

urlpatterns = [
    path('teacherhome', TeacherView.as_view(), name='studenthome'),
    path('materialmarket', MaterialMarketView.as_view(), name='materialmarket'),
]
