from django.urls import path

from . import views

urlpatterns = [
    path('', views.CompradorListView.as_view(), name='comprador_home'),
    path('<int:pk>/', views.CompradorDetailView.as_view(), name='comprador_detail'),
    path('new/', views.CompradorCreateView.as_view(), name='comprador_new'),
    path('<int:pk>/edit/',
         views.CompradorUpdateView.as_view(), name='comprador_edit'),
    path('<int:pk>/delete/',
         views.CompradorDeleteView.as_view(), name='comprador_delete'),
]