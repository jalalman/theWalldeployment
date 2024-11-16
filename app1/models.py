from django.db import models
import re

import bcrypt

class UserManger(models.Manager):

    def basic_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        if len(postData['fname'])<2:
            errors['fname']='the firstname should be at least 2'
        if len(postData['lname'])<2:
            errors['lname']='the lastname should be at least 2'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='not valid email'
        if len(postData['password']) <8:
            errors['password_len']="password should be at least 8"
        if postData['password'] != postData ['confirmpassword'] :
            errors['password']='password not match '



        return errors

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManger()

class Message(models.Model):
    messagecontent=models.TextField(default='')
    user=models.ForeignKey(User,related_name="messages",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    commentcontent=models.TextField(default='')
    message=models.ForeignKey(Message,related_name="comment",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="comment",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def addUser(data):

    password=data['password']
    pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
    User.objects.create(first_name=data['fname'],last_name=data['lname'],email=data['email'],password=pw_hash)


def AddMessageToUser(data):
    uid=data['uid']
    this_user=User.objects.get(id=int(uid))
    Message.objects.create(messagecontent=data['message'],user=this_user)

def getAllMessages():

    return Message.objects.all()

def addcommentToMessage(data):
    this_user=User.objects.get(id=int(data['uid']))
    this_message=Message.objects.get(id=int(data['mid']))
    Comment.objects.create(commentcontent=data['comment'],user=this_user,message=this_message)


def deleteByID(id):
    Message.objects.get(id=id).delete()

