from django.urls import path

from . import views

urlpatterns = [
    path('', views.LeiloeiroListView.as_view(), name='leiloeiro_home'),
    path('<int:pk>/', views.LeiloeiroDetailView.as_view(), name='leiloeiro_detail'),
    path('new/', views.LeiloeiroCreateView.as_view(), name='leiloeiro_new'),
    path('<int:pk>/edit/',
         views.LeiloeiroUpdateView.as_view(), name='leiloeiro_edit'),
    path('<int:pk>/delete/',
         views.LeiloeiroDeleteView.as_view(), name='leiloeiro_delete'),
]