from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=240)
    user_name = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.user_name + ' ' + self.user_lastname + '\n' + self.text + '\n' + self.date.strftime("%d/%m/%Y, %H:%M")


class Contact(models.Model):
    title = models.CharField(max_length=240)
    text = models.CharField(max_length=240)
    def __str__(self):
        return self.title + ' -- ' + self.text

class BotCommand(models.Model):
    command = models.CharField(max_length=20)
    description = models.CharField(max_length=240)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.command + ' -- ' + self.description
