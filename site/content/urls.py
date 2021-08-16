
from django.urls import path
from . import views

apps_name="content"

urlpatterns=[
    path('ho/',views.home,name="ho"),
]