from django.urls import path

from . import views

urlpatterns = [
    path('', views.VendedorListView.as_view(), name='vendedor_home'),
    path('<int:pk>/', views.VendedorDetailView.as_view(), name='vendedor_detail'),
    path('new/', views.VendedorCreateView.as_view(), name='vendedor_new'),
    path('<int:pk>/edit/',
         views.VendedorUpdateView.as_view(), name='vendedor_edit'),
    path('<int:pk>/delete/',
         views.VendedorDeleteView.as_view(), name='vendedor_delete'),
]