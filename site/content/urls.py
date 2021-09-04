
from django.urls import path
from . import views

app_name="contents"

urlpatterns=[
    path('',views.home,name='home'),
    path('detail/',views.detail,name='detail'),
]