from django.urls import path

from . import views

app_name ='accounts'

urlpatterns = [
    path('',views.login, name='login'),
    path('comment/',views.comment,name='comment'),
    path('profile/',views.profile,name='profile')
]
