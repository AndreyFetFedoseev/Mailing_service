from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingView, ClientCreateView, ClientUpdateView, ClientListView, ClientDetailView, \
    ClientDeleteView, MessageListView, MessageCreateView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingView.as_view(), name='base_mailing'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='update_client'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('message/create', MessageCreateView.as_view(), name='create_message'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='update_message'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
