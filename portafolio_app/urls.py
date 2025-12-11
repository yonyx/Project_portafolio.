from django.urls import path
from .views import HomeView, ProjectDetailView

app_name = "portafolio_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("proyecto/<slug:slug>/", ProjectDetailView.as_view(), name="project_detail"),
]
