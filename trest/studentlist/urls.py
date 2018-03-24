from django.urls import path
from . import views


app_name = 'studentlist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.details, name='details'),
]
