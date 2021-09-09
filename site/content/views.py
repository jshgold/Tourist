from django.shortcuts import render,redirect
from .models import Content
import pymysql
import random

def tourlist(request):
    if request.method=='GET':
        return render(request, 'content/tourlist.html')
    elif request.method=='POST':
        
        data= Content.objects.filter(yea=2010)



def home(request):
    if request.method == "GET":
        if request.session.get('user',''):
            juso=[]
            year=[]
            month=[]
            con = pymysql.connect(host="127.0.0.1" ,user="root" ,password="1234" ,db="site",charset="utf8")
            cur = con.cursor()
            sql = 'SELECT tourimg,spot FROM datas'
            cur.execute(sql)
            row=list(cur.fetchall())
            random.shuffle(row)
            lst=[]
            count=0
            for ro in row:
                if count==6:
                    break
                lst.append(ro)
                count+=1
            
            
            
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
            return render(request, 'content/home.html',{"searchs":juso,"years":year,"monthes":month,"rows":lst})
        else:
            return redirect('/signin')

    if request.method == "POST":
        plist=[]
        clist=[]
        tlist=[]
        dlist=[]
        
        place = request.POST.get('place',"")+'%'
        year = request.POST.get('ye',"")
        month = request.POST.get('month',"")
        

        con = pymysql.connect(host="127.0.0.1" ,user="root" ,password="1234" ,db="site",charset="utf8")
        cur = con.cursor()

        if place=="%" and month=="" and year=="":
            return redirect('/')

        elif month and place and year=="":
            sql= "SELECT * FROM datas WHERE mont=%s and dep LIKE %s"
            cur.execute(sql,(month,place))    
            row = cur.fetchall()

        elif year and place and month=="":
            sql= "SELECT * FROM datas WHERE yea=%s and dep LIKE %s"
            cur.execute(sql,(year,place))    
            row = cur.fetchall()

        elif year and month and place=="%":
            sql= "SELECT * FROM datas WHERE yea=%s and mont=%s"
            cur.execute(sql,(year,month))    
            row = cur.fetchall()

        elif year and place==month :
            sql= "SELECT * FROM datas WHERE yea=%s "
            cur.execute(sql,(year))    
            row = cur.fetchall()

        elif place and year==month:
            sql= "SELECT * FROM datas WHERE dep LIKE %s "
            cur.execute(sql,(place))    
            row = cur.fetchall()
        
        elif month and year==place:
            sql= "SELECT * FROM datas WHERE month=%s "
            cur.execute(sql,(month))    
            row = cur.fetchall()

        
        elif place !="" and month!="" and year!="":   
            sql = "SELECT * FROM datas WHERE yea=%s and mont=%s and dep LIKE %s"
            cur.execute(sql,(year,month,place))
            row = cur.fetchall()
        
        

        for ro in row:
            plist.append(ro[0])
            clist.append(ro[1])
            tlist.append(ro[2])
            dlist.append(ro[3])
        
        counts=len(plist)
        total=[[] for _ in range(counts)]
        for count in range(counts):
            total[count].append(plist[count])
            total[count].append(clist[count])
            total[count].append(tlist[count])
            total[count].append(dlist[count])
        
        return render(request,'content/result.html',{"places":total})



def detail(request):
    if request.method=="GET":
        spotname= request.GET.get('spotname','')
        con = pymysql.connect(host="127.0.0.1",user="root",password="1234",db="site",charset="utf8")
        cur=con.cursor()
        sql= "SELECT tourimg,spot,cont,dep FROM datas WHERE spot = %s"
        cur.execute(sql,(spotname))
        row=cur.fetchall()

        return render(request,'content/detail.html',{"rows":row})
    

   




    
    

    
    
            


        

        


