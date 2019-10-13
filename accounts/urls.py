from django.urls import path

from . import views

app_name ='accounts'

urlpatterns = [
    path('',views.login, name='login'),
    path('comment/',views.comment,name='comment'),
    path('profile/',views.profile,name='profile'),
    path('pincomment/',views.pincomment,name='pincomment'),
    path('image/',views.imageRegister,name = 'imageHandler'),
    path('image/<str:name>/',views.imageResponse,name='imagehandler'),
    path('register/',views.register,name='register')

]
