from django.urls import path
from . import views

app_name="members"

urlpatterns =[
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('',views.home,name='home'),
]