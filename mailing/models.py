from django.db import models

NULLABLE = {"null": True, "blank": True}


# Create your models here.
class Client(models.Model):
    """
    Модель клиента сервиса
    """

    name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(max_length=100, verbose_name="почта", unique=True)
    comments = models.TextField(verbose_name="Комментарии", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    """
    Модель сообщения
    """

    title = models.CharField(
        max_length=100, verbose_name="Заголовок сообщения", **NULLABLE
    )
    content = models.TextField(verbose_name="Содержание сообщения", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    """
    Модель рассылки
    """

    date = models.DateField(verbose_name="Дата рассылки", auto_now_add=True)
    status = models.CharField(max_length=100, verbose_name="Статус рассылки")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиенты")
    message = models.OneToOneField(
        Message, on_delete=models.SET_NULL, verbose_name="Сообщение", **NULLABLE
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class AttemptMailing(models.Model):
    """
    Модель попытки рассылки
    """

    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка"
    )
    date = models.DateField(verbose_name="Дата попытки рассылки", auto_now_add=True)
    status = models.BooleanField(verbose_name="Статус попытки рассылки", default=False)
    answer = models.TextField(verbose_name="Ответ сервиса", **NULLABLE)

    def __str__(self):
        return self.mailing.name

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
