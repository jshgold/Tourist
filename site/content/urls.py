
from django.urls import path
from . import views

apps_name="contents"

urlpatterns=[
    path('tourlist/',views.tourlist,name="tourlist"),
    path('search/',views.search,name="search"),
    path('',views.home,name='home'),
]