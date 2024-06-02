from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView, DeleteView

from mailing.models import Client, Message


# Create your views here.
class MailingView(TemplateView):
    template_name = "mailing/base_mailing.html"


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comments')
    success_url = reverse_lazy('mailing:clients')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comments')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'content')
    success_url = reverse_lazy('mailing:messages')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'content')


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')
