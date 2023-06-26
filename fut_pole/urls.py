from django.urls import path
from . import views

urlpatterns = [
    path('fields/', views.field_list, name='field_list'),
]