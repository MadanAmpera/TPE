from django.urls import path

from . import views


app_name = 'progress_app'
urlpatterns = [
    #index
    path('', views.index, name='index'),
    #login
    path('login/', views.login, name='login'),
    #Admin dashboard
    path('admin/', views.adminBoard, name='admin'),
    #Student registration
    path('studentreg/', views.studentReg, name='studentreg'),
]
