from django.conf.urls import url
from program import views

urlpatterns = [
    url(r'^$', views.ProgramView.as_view(), name='index'),
    url(r'block_trade/$', views.BlockTradeView.as_view(), name='block_trade'),
    url(r'executive/$', views.ExecutiveRegulationView.as_view(), name='executive'),
    url(r'announcement/$', views.HKStockAnnouncementView.as_view(), name='announcement'),
    url(r'stock_equity/$', views.HKStockEquityView.as_view(), name='stock_equity'),
    url(r'margin_trade/$', views.MarginTradeView.as_view(), name='margin_trade'),
    url(r'report/$', views.ReportView.as_view(), name='report'),
]
