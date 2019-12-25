from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tania-dika/', views.tania_dika_index, name='tania_dika'),
    path('tania-dika/<int:param_id>/<str:param_guest_name>', views.tania_dika_invitation, name='tania_dika_invitation'),
    path('tania-dika/submit-message/<int:param_id>/<str:param_guest_name>', views.tania_dika_submit_message, name='submit_message'),
]