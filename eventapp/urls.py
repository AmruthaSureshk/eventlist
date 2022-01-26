from . import views
from django.urls import path

app_name = 'eventapp'
urlpatterns = [

    path('', views.index, name='index'),

]
