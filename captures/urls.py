from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_captures, name='captures'),
    path('<capture_id>', views.capture_detail, name='capture_detail'),
    path('<int:capture_id>/', views.capture_detail, name='capture_detail'),
    path('add/', views.add_capture, name='add_capture'),
]
