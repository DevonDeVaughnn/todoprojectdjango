from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('todo/', views.activities_list, name="activities_list"),
    path('activitydetail/<int:id>', views.activityDetail, name="activity"),
    path('newactivity/', views.newActivity, name="newactivity"),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

    path('accounts/', include('django.contrib.auth.urls')),
]
