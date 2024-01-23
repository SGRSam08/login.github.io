from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def forgotaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Samuel@120",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="password":
                pwd=value

        c="update users set password='{}' where email='{}'".format(em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'forgot_page.html')