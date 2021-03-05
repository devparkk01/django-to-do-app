from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.home_view , name = "home" ) , 
    path('add-item/' , views.add_item , name = "add-item") ,
    path('delete-item/<int:id>/' , views.delete_item , name = "delete-item")  , 
    path('change-status/<int:id>/<str:status>/' , views.change_status , name = 'change-status') ,
    path('login/' , views.login_view  , name = "login") ,
    path('delete-all/<str:username>/' , views.delete_all , name = 'delete-all') , 
    path('delete-completed/<str:username>/' , views.delete_completed , name = "delete-completed") , 
    path('register/' , views.register_view , name = "register") ,
    path('logout/' , views.logout_view , name = "logout") , 

]
