from django import forms
from .models import Message
from django.utils.translation import ugettext_lazy as _

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ( 'user_name', 'text', 'contact')
        labels = {
            'text': _('Сообщение'),
            'user_name': _('Имя'),
            'contact': _('Контактные данные')
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
