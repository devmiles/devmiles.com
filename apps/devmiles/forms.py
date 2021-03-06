from django.forms import ModelForm
from devmiles.models import QuoteRequest
from django.forms.widgets import Textarea

class RequestQuoteForm(ModelForm):
    class Meta:
        model = QuoteRequest
        widgets = {
            'message': Textarea(attrs={'cols':40, 'rows': 6})
        }

class MessageForm(ModelForm):
    class Meta:
        model = QuoteRequest
        exclude = ('company', 'phone')
        widgets = {
            'message': Textarea(attrs={'cols':40, 'rows': 6})
        }