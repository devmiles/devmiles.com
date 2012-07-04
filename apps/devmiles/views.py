from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from devmiles.forms import RequestQuoteForm
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.utils import simplejson
from django.core.context_processors import csrf
from django.core.mail import send_mass_mail, send_mail
#from mailer import send_mail
from django.contrib.auth.models import User

def home(request):
    form = RequestQuoteForm()
    return render_to_response('devmiles_base.html', {'form': form}, context_instance=RequestContext(request))

@require_POST
def quote(request):
    form = RequestQuoteForm(request.POST)
    c = {}
    #c.
    if form.is_valid():
        new_quote_request = form.save()
        recipients = User.objects.filter(is_staff=True).values_list('email', flat=True)
        send_mail('Quote requested', new_quote_request.message, 'zgollum@gmail.com', recipients, False)
        #mail_admins('Quote requested', new_quote_request.message)
        context = {'form': form}
        context.update(csrf(request))
        rendered = render_to_string('requestquoteform.html', context)
        json = { 'status' : 'ok', 'html': rendered }
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')
    else:
        context = {'form': form}
        context.update(csrf(request))
        rendered = render_to_string('requestquoteform.html', context)
        json = { 'status' : 'error', 'html': rendered }
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')