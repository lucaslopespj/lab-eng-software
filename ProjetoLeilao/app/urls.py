from django.urls import path

from . import views

urlpatterns = [

    #Views Comprador
    path('comprador/', views.CompradorListView.as_view(), name='comprador_home'),
    path('comprador/<int:pk>/', views.CompradorDetailView.as_view(), name='comprador_detail'),
    path('comprador/new/', views.CompradorCreateView.as_view(), name='comprador_new'),
    path('comprador/<int:pk>/edit/',
         views.CompradorUpdateView.as_view(), name='comprador_edit'),
    path('comprador/<int:pk>/delete/',
         views.CompradorDeleteView.as_view(), name='comprador_delete'),

    #Views Leiloeiro
    path('leiloeiro/', views.LeiloeiroListView.as_view(), name='leiloeiro_home'),
    path('leiloeiro/<int:pk>/', views.LeiloeiroDetailView.as_view(), name='leiloeiro_detail'),
    path('leiloeiro/new/', views.LeiloeiroCreateView.as_view(), name='leiloeiro_new'),
    path('leiloeiro/<int:pk>/edit/',
         views.LeiloeiroUpdateView.as_view(), name='leiloeiro_edit'),
    path('leiloeiro/<int:pk>/delete/',
         views.LeiloeiroDeleteView.as_view(), name='leiloeiro_delete'),

    #Views Vendedor
    path('vendedor/', views.VendedorListView.as_view(), name='vendedor_home'),
    path('vendedor/<int:pk>/', views.VendedorDetailView.as_view(), name='vendedor_detail'),
    path('vendedor/new/', views.VendedorCreateView.as_view(), name='vendedor_new'),
    path('vendedor/<int:pk>/edit/',
         views.VendedorUpdateView.as_view(), name='vendedor_edit'),
    path('vendedor/<int:pk>/delete/',
         views.VendedorDeleteView.as_view(), name='vendedor_delete'),

    #Home Page
    path('', views.HomeView.as_view(), name='home'),
]