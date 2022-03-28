#helper funciton from django to help define different paths in our app
from django.urls import path 
#imports views
from user import views 

app_name = 'user'

urlpatterns = [
  path('create/', views.CreateUserView.as_view(), name='create'),
]
#update urls.py in app/app/urls.py