from django.shortcuts import render
from .models import Contact
# Create your views here.
link_text = lambda href: href.split('/')[-1]

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
