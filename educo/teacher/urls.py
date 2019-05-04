from django.urls import path

from .views import TeacherView, MaterialMarketView, TeacherDashView, TeacherAnalysisManageView

urlpatterns = [
    path('teacherhome', TeacherView.as_view(), name='studenthome'),
    path('materialmarket', MaterialMarketView.as_view(), name='materialmarket'),
    path('dash', TeacherDashView.as_view(), name='teacherdash'),
    path('analysis_manage', TeacherAnalysisManageView.as_view(), name='analysis_manage'),
]
