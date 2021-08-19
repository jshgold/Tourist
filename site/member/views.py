from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse
from django.db import connection
from .models import User
from content.models import Content
import datetime
import requests


def signup(request):
    if request.method == 'GET':
        return render(request, "member/signup.html")

    elif request.method =="POST":
        userid = request.POST.get('userid',None)
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)

        res_data={}
        if not(userid and email and password and re_password):

            res_data['error']="전부 입력 요망"

        elif password != re_password:
            res_data['error'] = "비밀번호가 다름"
        
        else:
            user = User(
                userid = userid,
                email = email,
                password = make_password(password),
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now()
            )
            user.save()

        return render(request, 'member/signup.html',res_data)

    


def signin(request):
    if request.method=="GET":
        return render(request, 'member/signin.html')
    
    elif request.method=="POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        res_data={}
        if not (userid and password):
            res_data['error']="모두 입력 하세요"
        
        else:
            user = User.objects.get(userid=userid)

            if check_password(password, user.password):
                request.session['user']= user.userid
                return redirect('/')

            else:
                res_data['error'] = "비밀번호가 틀림"
        
        return render(request , 'member/signin.html',res_data)


def home(request):
    

    return render(request, 'member/home.html')


        
    
    


def signout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


        
