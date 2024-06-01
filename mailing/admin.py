from django.contrib import admin

from mailing.models import Client, Message, Mailing, AttemptMailing


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "comments",
    )
    list_filter = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
    )
    list_filter = ('title',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "status",
        "client",
        "message",
    )
    list_filter = ('date', 'status', 'client',)


@admin.register(AttemptMailing)
class AttemptMailingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mailing",
        "status",
        "date",
        "answer",
    )
    list_filter = ('status',)
