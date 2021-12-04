from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('lote/<int:pk>/', views.LoteDetailView.as_view(), name="lote_detail"),
    path('lote/add/', views.LoteAddView.as_view(), name="lote_add"),
    path('lote/lance/<int:pk>/', views.LoteLanceView.as_view(), name="lote_lance"),
    path('lote/editar/<int:pk>/', views.LoteEditarView.as_view(), name="lote_editar"),
    path('lote/editaradm/<int:pk>/', views.LoteEditarAdmView.as_view(), name="lote_editar_adm"),
    path('lote/finalizar/<int:pk>/', views.LoteFinalizarLeilaoView.as_view(), name="lote_finalizar"),
    path('lote/liberar/<int:pk>', views.LoteLiberarView.as_view(), name="lote_liberar"),
    path('lote/cancel/<int:pk>/', views.LoteCancelView.as_view(), name="lote_cancel"),
    path('saldo/update/', views.SaldoUpdateView.as_view(), name="saldo_update"),
    path('saldo/confere/', views.SaldoCheckView.as_view(), name="saldo_check"),
    path('exclusiva/', views.AreaExclusivaView.as_view(), name='area_exclusiva'),
    path('exclusiva/faturamento/gerar/', views.GerarRelatorioFaturamentoView.as_view(), name='gerar_relatorio_faturamento'),
    path('exclusiva/faturamento/gerar/visualizar/', views.RelatorioFaturamentoView.as_view(), name='relatorio_faturamento'),
    path('exclusiva/desempenho/gerar/', views.GerarRelatorioDesempenhoView.as_view(), name='gerar_relatorio_desempenho'),
    path('exclusiva/desempenho/gerar/visualizar', views.RelatorioDesempenhoView.as_view(), name='relatorio_desempenho'),
]