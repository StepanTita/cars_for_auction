from django.urls import path

from prediction import views

urlpatterns = [
    path('', views.PredictView.as_view()),
]
