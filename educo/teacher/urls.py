from django.urls import path

from .views import *


urlpatterns = [
    path('teacherhome', TeacherView.as_view(), name='studenthome'),
    path('materialmarket', MaterialMarketView.as_view(), name='materialmarket'),
    path('materialcontent', MaterialContentView.as_view(), name='materialcontent'),
    path('filtered', FilteredMaterialContentView.as_view(), name='filtered'),
    path('dash', TeacherDashView.as_view(), name='teacherdash'),
    path('analysis_manage', TeacherAnalysisManageView.as_view(), name='analysis_manage'),
]
