from django.urls import path

from . import views


urlpatterns=[

    path('',views.home,name='home'),
    path('regAcc',views.regAcc,name='regAcc'),
    path('confirmlogin',views.confirmlogin,name='confirmlogin'),
    path('success',views.suclogin,name='suclogin'),
    path('logout',views.logout,name='logout'),
    path('postmsg',views.postmsg,name='postmsg'),
    path('addcomment',views.addcomment,name="addcomment"),
    path('deletemsg/<int:id>',views.deletemsg,name='deletemsg')


]