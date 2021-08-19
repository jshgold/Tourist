from django.shortcuts import render
from .models import Content
from django.db import connection
import pymysql

def tourlist(request):
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

    return render(request, 'content/tourlist.html',{'lst':datas})

def search(request):
    juso=[]
    year=[]
    month=[]
    con = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="site",charset="utf8")
    cur = con.cursor()
    sql = "SELECT dep FROM datas"
    cur.execute(sql)
    while(True):
        row=cur.fetchone()
        if row==None:
            break
        row=row[0]
        space=row.find(" ")
        if row.startswith("충북"):
            row=row.replace(row[:space],"충청북도")
            space=row.find(" ")
        elif row.startswith("충남"):
            row=row.replace(row[:space],"충청남도")
            space=row.find(" ")
        elif row.startswith("경북"):
            row=row.replace(row[:space],"경상북도")
            space=row.find(" ")
        elif row.startswith("경남"):
            row=row.replace(row[:space],"경상남도")
            space=row.find(" ")
        elif row.startswith("전북"):
            row=row.replace(row[:space],"전라북도")
            space=row.find(" ")
        elif row.startswith("전남"):
            row=row.replace(row[:space],"전라남도")
            space=row.find(" ")
        elif row.startswith("서울시"):
            row=row.replace(row[:space],"서울특별시")
            space=row.find(" ")
        elif row.startswith("제주도"):
            row=row.replace(row[:space],"제주시")
            space=row.find(" ")

        if row[:space] not in juso:
            juso.append(row[:space])
    cur = con.cursor()
    sql = "SELECT yea FROM datas"
    cur.execute(sql)
    while(True):
        row=cur.fetchone()
        if row==None:
            break
        row=row[0]
        if row not in year:
            year.append(row)
    
    cur = con.cursor()
    sql = "SELECT mont FROM datas"
    cur.execute(sql)
    while(True):
        row=cur.fetchone()
        if row==None:
            break
        row=row[0]
        if row not in month:
            month.append(row)
    juso.sort()
    month.sort()
    year.sort()
    return render(request, 'content/search.html',{"searchs":juso,"years":year,"monthes":month})


