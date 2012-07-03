from django.forms import ModelForm
from devmiles.models import QuoteRequest

class RequestQuoteForm(ModelForm):
    class Meta:
        model = QuoteRequest