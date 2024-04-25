from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_disaster, name='report_disaster'),
]
