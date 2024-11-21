from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# import mysql.connector as sql



def Shivhome(request):

    return render (request, 'Shiv.html')

def Aboutpage(request):

    return render (request, 'about.html')

def Confipage(request):

    return render (request, 'loage.html')

def Missionpage(request):

    return render (request, 'mission.html')

def Memberpage(request):

    return render (request, 'members.html')


def Achievementpage(request):

    return render (request, 'achievement.html')

def Signuppage(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        Email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse('password are not same ')
        else:
            my_user=User.objects.create_user(uname,Email,pass1)
            my_user.save()
           
            return redirect('Home')
        
    return render (request, 'Signup.html')

def Loginpage(request):
    if request.method == 'POST':
         user=request.POST.get('username')
         pass1=request.POST.get('password')
         user=authenticate(request, username=user,password=pass1)
         if user is not None:
            login(request, user)
            return redirect('Config')
         else:
            return HttpResponse("password doesn't match")

        #  print(user,pass1)

    return render (request, 'shivlog.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
# fn=''
# ln=''
# em=''
# pwd=''


# def form(request):
#     global fn,ln,em,pwd
#     if request.method=="POST":
#         m=sql.connect(host='localhost',user='root',password='Tarun@9927',database='mohit')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=='First_name':
#                 fn=value
#             if key=='Last_name':
#                 ln=value
#             if key=='Email':
#                 em=value
#             if key=='Password':
#                 pwd=value
#         c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)                   
#         cursor.execute(c)
#         m.commit()
#     return render (request,"form.html")    

   
