from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('contas/', include('django.contrib.auth.urls')),
    path('contas/signup/', views.SignUpView.as_view(), name='signup'),
    path('contas/signup/leiloeiro/', views.LeiloeiroSignUpView.as_view(), name='leiloeiro_signup'),
    path('contas/signup/cliente/', views.ClienteSignUpView.as_view(), name='cliente_signup'),
]