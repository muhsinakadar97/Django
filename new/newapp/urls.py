from django.urls import path
from newapp import views

urlpatterns = [
	path('', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    
]
