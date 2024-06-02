from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingView, ClientCreateView, ClientUpdateView, ClientListView, ClientDetailView, \
    ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingView.as_view(), name='base_mailing'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='update_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
