from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_captures, name='captures'),
    path('<int:capture_id>/', views.capture_detail, name='capture_detail'),
]
