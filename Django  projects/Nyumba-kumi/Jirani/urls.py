from django.urls import path
from . import views

urlpatterns=[
  path('', views.index, name='index'),
  path('search/', views.search_results, name='search_results'),
  path('new_neighbourhood/', views.create_neighbourhood, name='new_neighbourhood'),
  path('neighbourhoods/', views.neighbourhoods, name='neighbourhoods'),
  path('join_neighbourhood/<int:pk>', views.join_neighbourhood, name='join_neighbourhood'),
  path('change_neighbourhood/<int:pk>', views.change_neighbourhood, name='change_neighbourhood'),
  path('neighbourhood/<int:pk>', views.neighbourhood_details, name='neighbourhood_details'),
  path('new_business/<int:pk>', views.create_business, name='create_business'),
]