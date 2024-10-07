from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.homefunction,name='home'),
    path('superhome',views.superhome,name='superhome'),
    path('createadmin',views.createadmin,name='createadmin'),
    path('logout',views.logoutfunction,name='logout'),
    path('delete<int:id>',views.deletefunction,name='delete'),
    path('edit<int:id>',views.editfunction,name='edit'),

]