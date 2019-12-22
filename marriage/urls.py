from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tania-dika/', views.tania_dika_index, name='tania_dika'),
    path('tania-dika/<str:guest_name>', views.tania_dika_invitation, name='tania_dika'),
]