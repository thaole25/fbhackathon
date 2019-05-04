from django.urls import path

from .views import TeacherView, MaterialMarketView

urlpatterns = [
<<<<<<< HEAD
    path('teacherhome', TeacherView.as_view(), name='studenthome'),
    path('materialmarket', MaterialMarketView.as_view(), name='materialmarket'),
=======
    path('teacherhome', TeacherView.as_view(), name='teacherhome'),
>>>>>>> 06c30511b8925fbb42852acb01b997682972a646
]
