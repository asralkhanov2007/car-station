from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('',views.homePage,name='home'),
	path('grafik',views.grafik,name='grafik'),
	path('transports/',views.TransportPageView.as_view(),name='transports'),
    path('category/<slug:category_slug>',views.categoryDetailPage,name='category_detail'),
    path('detail/<pk>',views.TransportDetailView.as_view(),name='transport_detail'),
	path('contact/',views.contactPage,name='contact'),
]