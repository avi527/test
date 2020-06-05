from django.urls import path,include
from ThrottleApp import views
urlpatterns = [
    path('home/<id>/',views.home, name='home'),
]
