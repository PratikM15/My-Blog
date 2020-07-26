from django.conf.urls import include, url
from django.urls import path

from.import views

urlpatterns = [
    path('addblog', views.createBlog, name ="create"),
    path('',views.index),
    path('login', views.login_user),
    path('signup',views.signup),
    path('logout',views.logout_user),

]