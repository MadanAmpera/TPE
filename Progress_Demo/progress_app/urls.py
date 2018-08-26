from django.urls import path

from . import views


app_name = 'progress_app'
urlpatterns = [
    path('', views.students_show, name='students_show'),
    path('<int:student_id>/', views.progress_view, name='progress_view'),
]