from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ClientList.as_view()),
    path('<int:pk>/', views.ClientDetail.as_view()),
    path('addresses/', views.AddressList.as_view()),
    path('address/<int:pk>/', views.AddressDetail.as_view()),
]