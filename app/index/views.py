from django.shortcuts import render
from .models import Contact, BotCommand
# Create your views here.
link_text = lambda href: href.split('/')[-1]

# Главная страница (удалить лишнее!)
def index(request):
    contact_list = Contact.objects.all()
    for contact in contact_list:
        link = link_text(contact.text)
        if(link != contact.text):
            contact.link = link
    return render(
      request,
      'index.html',
      context=
      {'contact_list': contact_list}
    )

# Страница с информацией о боте
def botList(request):
    command_list = BotCommand.objects.all()
    return render(
      request,
      'bot_list.html',
      context=
        {'command_list': command_list}
    )
# Страница контактов -- для ссылок дополнительно формируется текст в лямбда функции
def contacts(request):
    contact_list = Contact.objects.all()
    for contact in contact_list:
        link = link_text(contact.text)
        if(link != contact.text):
            contact.link = link
    return render(
      request,
      'contacts.html',
      context=
      {'contact_list': contact_list}
    )

#Форма отправки сообщения в бота
def messageForm(request):
    return(
      request,
      'message_form.html'
    )
