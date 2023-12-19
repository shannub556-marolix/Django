from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.taskapp,name='task'),
    path('details',views.details,name='details'),
]