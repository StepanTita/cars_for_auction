from django.urls import path

from prediction import views

urlpatterns = [
    path('', views.PriceView.as_view(), name='main-view'),
    path('predict/', views.PredictView.as_view(), name='prediction-view'),
    path('version/', views.VersionView.as_view(), name='version-view')
]
