from django.shortcuts import render
from .models import Content
from django.db import connection

def home(request):
    datas = Content.objects.all()
    #lst=[]
    #try:
    #    cursor = connection.cursor()
#
    #    strSql = "SELECT spot,cont,tourimg,dep"
    #    result = cursor.execute(strSql)
    #    datas = cursor.fetchall()
#
    #    connection.commit()
    #    connection.close()
#
    #    
    #    for data in datas:
    #        row = {
    #            'spot' : data[0],
    #            'cont': data[1],
    #            'tourimg': data[2],
    #            'dep': data[3]
    #            }
    #        lst.append(row)
    #
    #except:
    #    connection.rollback()
    #    print("failed")

    return render(request, 'content/home.html',{'lst':datas})
