# urls.py
from django.urls import path
from . import views
app_name="formapp"

urlpatterns = [
    path('student-form/', views.student_form, name='student_form'),
    path('odercom/', views.odercom, name='odercom'),



]
