from django.shortcuts import render
from default.models import Todolist
from default.models import User
from default.models import Peoson



# Create your views here.

def log(request):
    return render(request, 'log.html')

def reg(request):
    return render(request, 'reg.html')

def reging(requset):
    if requset.method == 'POST':
        vname = requset.POST['UserName']
        vpassword = requset.POST['Password']
        u = User(name=vname, password=vpassword)
        u.save()
        peolist = Peoson.objects.all()
        return render(requset,'getlist.html',{'peolist':peolist})

def loging(request):
    if request.method =='POST':
     users = User.objects.all()
     visiterName = request.POST['UserName']
     visiterPassword = request.POST['Password']
    for i in users:
        if ((visiterName == i.name) and (visiterPassword == i.password)):
         peolist = Peoson.objects.all()
         return render(request,'getlist.html',{'peolist':peolist})
    else:
        return render(request,'log.html')



def getlist(request):
    peolist = Peoson.objects.all()
    return render(request,'getlist.html',{'peolist':peolist})

def addlist(request):
    if request.method == 'GET':
        return render(request,'addlist.html')
    elif request.method =='POST':
        na = request.POST['name']
        peo = Peoson(name=na)
        peo.save()
        peolist = Peoson.objects.all()
        return render(request,'getlist.html',{'peolist':peolist})

def updatelist(request):
    if request.method == 'GET':
        peoid = request.GET['peoid']
        peo = Peoson.objects.get(id=peoid)
        return render(request,'updatelist.html',{'peo':peo})
    elif request.method == 'POST':
        peoid = request.POST['id']
        name = request.POST['name']
        phonenum = request.POST['phonenum']
        email = request.POST['email']
        address = request.POST['address']
        qq = request.POST['qq']
        peo = Peoson.objects.get(id=peoid)
        peo.name = name
        peo.phonenum = phonenum
        peo.email = email
        peo.address = address
        peo.qq = qq
        peo.save()
        peolist = Peoson.objects.all()
        return render(request,'getlist.html',{'peolist':peolist})


def dellist(request):
    peoid = request.GET['peoid']
    Peoson.objects.get(id=peoid).delete()
    peolist = Peoson.objects.all()
    return render(request,'getlist.html',{'peolist':peolist})

def more(request):
    if request.method == 'GET':
        peoid = request.GET['peoid']
        peo = Peoson.objects.get(id=peoid)
        return render(request,'more.html',{'peo':peo})
    elif request.method == 'POST':
        peolist = Peoson.objects.all()
        return render(request,'getlist.html',{'peolist':peolist})

def find(request):
    if request.method == 'GET':
        return render(request,'find.html')
    elif request.method == 'POST':
        name = request.POST['name']
        peolist = Peoson.objects.all()
        for p in peolist:
            if (p.name == name):
                return render(request,'updatelist.html',{'peo':p})
        return render(request,'getlist.html',{'peolist':peolist})