from django.shortcuts import render,redirect
from .models import Content
import pymysql

def tourlist(request):
    if request.method=='GET':
        return render(request, 'content/tourlist.html')
    elif request.method=='POST':
        
        data= Content.objects.filter(yea=2010)

def search(request):
    if request.method == 'GET':
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
            elif row.startswith("서울"):
                row=row.replace(row[:space],"서울특별시")
                space=row.find(" ")

            elif row.startswith("제주"):
                row=row.replace(row[:space],"제주시")
                space=row.find(" ")
            elif row.startswith("강원"):
                row=row.replace(row[:space],"강원도")
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

    elif request.method =="POST":
        do=[]
        place = request.POST.get('PlaceValue')+'%'
        year = request.POST.get('YearValue')
        month = request.POST.get('MonthValue')
        con = pymysql.connect(host="127.0.0.1" ,user="root" ,password="1234" ,db="site",charset="utf8")
        cur = con.cursor()
        sql = "SELECT * FROM datas WHERE yea=%s and mont=%s and dep LIKE %s"
        cur.execute(sql,(year,month,place))
        row = cur.fetchall()
        for ro in row:
            place=ro[0]
            cont = ro[1]
            tourimg = ro[2]
            dep = ro[3]

        
        return render(request,'content/tourlist.html',{"place":place,"cont":cont,"tourimg":tourimg,"dep":dep})
            

        

        

        


