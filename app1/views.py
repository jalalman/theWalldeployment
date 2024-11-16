from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib import messages
import bcrypt
from .models import User ,Message,Comment
from . import models
# Create your views here.
def home(request):


    return render(request,'loginandreg.html')


def regAcc(request):
    if request.method=="POST":
        errors=User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)

            return redirect('/')

        else:
            models.addUser(request.POST)
            return redirect('/')

def confirmlogin(request):
    if request.method=="POST":
        email=User.objects.filter(email=request.POST['email']).first()

        if email:
            if bcrypt.checkpw(request.POST['password'].encode(),email.password.encode()):
                request.session['fname']=email.first_name
                request.session['id']=int(email.id)

                return redirect('/success')

    return redirect('/')


def suclogin(request):
    context={
        "messages":models.getAllMessages(),

    }

    return render(request,'wallpage.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

def postmsg(request):
    if request.method=='POST':
        models.AddMessageToUser(request.POST)
        return redirect('/success')
    else:
        return HttpResponse('error')

def addcomment(request):
    if request.method=="POST":
        models.addcommentToMessage(request.POST)
        return redirect('/success',request.POST['mid'])
    else:
        return HttpResponse('error')

def deletemsg(request,id):
    message = Message.objects.get(id=id)

    if int(request.session['id']) == message.user.id:
        message.delete()
    return redirect('/success')