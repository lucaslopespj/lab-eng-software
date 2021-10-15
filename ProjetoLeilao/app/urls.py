from django.urls import include, path
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

     #Views Lote
     path('lote/', views.LoteListView.as_view(), name='lote_home'),
     path('lote/<int:pk>/', views.LoteDetailView.as_view(), name='lote_detail'),
     path('lote/new/', views.LoteCreateView.as_view(), name='formulario_ofertar_novo_lote'),
     path('lote/<int:pk>/edit/',
         views.LoteUpdateView.as_view(), name='lote_edit'),
     path('lote/<int:pk>/delete/',
         views.LoteDeleteView.as_view(), name='lote_delete'),

    #Home Page
    path('', views.HomeView.as_view(), name='home'),

    #Cadastro
    path('contas/', include('django.contrib.auth.urls')),
    path('contas/cadastrar/', views.SignUpView.as_view(), name='cadastrar'),
    path('contas/cadastrar/cliente/', views.CadastrarClienteView.as_view(), name='cadastrar_cliente'),
    path('contas/cadastrar/admin/', views.CadastrarAdminView.as_view(), name='cadastrar_admin'),
]