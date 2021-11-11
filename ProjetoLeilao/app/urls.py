from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('exclusiva/', views.AreaExclusivaView.as_view(), name='area_exclusiva'),
    path('lote/<int:pk>/', views.LoteDetailView.as_view(), name="lote_detail"),
    path('lote/add/', views.LoteAddView.as_view(), name="lote_add"),
    path('lote/lance/<int:pk>/', views.LoteLanceView.as_view(), name="lote_lance"),
    path('lote/liberar/<int:pk>', views.LoteLiberarView.as_view(), name="lote_liberar"),
    path('lote/cancel/<int:pk>/', views.LoteCancelView.as_view(), name="lote_cancel"),
    path('saldo/update/', views.SaldoUpdateView.as_view(), name="saldo_update"),
    path('saldo/confere/', views.SaldoCheckView.as_view(), name="saldo_check"),
    path('exclusiva/relatorio/', views.RelatorioView.as_view(), name='relatorio'),
]