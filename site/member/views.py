from django.shortcuts import render

def signup(request):
    return render(request, 'member/signup.html')


def signin(request):
    return render(request, 'member/signin.html')
