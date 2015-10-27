from django.conf.urls import url
from program import views

urlpatterns = [
    url(r'^$', views.Program.as_view(), name='index'),
    url(r'margin_trade/$', views.BlockTrade.as_view(), name='margin_trade'),
]
