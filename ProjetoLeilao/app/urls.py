from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('exclusiva/', views.AreaExclusivaView.as_view(), name='area_exclusiva'),
    path('lote/<int:pk>/', views.LoteDetailView.as_view(), name="lote_detail"),
    path('lote/add/', views.LoteAddView.as_view(), name="lote_add"),
    path('lote/lance/<int:pk>/', views.LoteLanceView.as_view(), name="lote_lance"),
]