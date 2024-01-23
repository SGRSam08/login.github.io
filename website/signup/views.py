from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
b=''
h=''
n=''
em=''
pwd=''

def signaction(request):
    global fn,ln,s,b,h,n,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Samuel@120",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="dob":
                b=value
            if key=="hobbies":
                h=value
            if key=="music":
                n=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,s,b,h,n,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')