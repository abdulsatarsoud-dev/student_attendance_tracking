from django.urls import path
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

from django.urls import path
from .views import HomeView, StudentListView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", StudentListView.as_view(), name="about"),
]
