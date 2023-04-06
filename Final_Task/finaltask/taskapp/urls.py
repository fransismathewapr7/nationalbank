from . import views
from django.urls import path
app_name="taskapp"

urlpatterns = [

    path('',views.demo,name='demo'),

]