from django.urls import path
from . import views

urlpatterns = [
    path("analyze_resume/", views.analyze_resume, name="analyze_resume"),
]
