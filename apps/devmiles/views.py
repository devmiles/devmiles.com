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
from apps.devmiles.forms import MessageForm
from settings import DEFAULT_FROM_EMAIL

def home(request):
    form = RequestQuoteForm()
    messageform = MessageForm()
    return render_to_response('devmiles_base.html', {'form': form, 'messageform': messageform}, context_instance=RequestContext(request))

@require_POST
def quote(request, type='message'):
    template_names = {'message': 'messageform.html', 'quote': 'requestquoteform.html'}
    if (type == 'quote'):
        form = RequestQuoteForm(request.POST)
    else:
        form = MessageForm(request.POST)
    if form.is_valid():
        new_quote_request = form.save()
        recipients = User.objects.filter(is_staff=True).values_list('email', flat=True)
        # construct a notification
        notification = """New quote request received from %(name)s.
        Email: %(email)s
        Company: %(company)s
        Phone: %(phone)s
        Message: %(message)s
        Date: %(created_at)s
        """ % {'name': new_quote_request.name, 'email': new_quote_request.email, 'company': new_quote_request.company,
               'phone': new_quote_request.phone, 'message': new_quote_request.message, 'created_at': new_quote_request.created_at}
        send_mail('Quote requested', notification, DEFAULT_FROM_EMAIL, recipients, False)
        #mail_admins('Quote requested', new_quote_request.message)
        if (type == 'quote'):
            form = RequestQuoteForm()
            context = {'form': form}
        else:
            form = MessageForm()
            context = {'messageform': form}
        context.update(csrf(request))
        rendered = render_to_string(template_names[type], context)
        json = { 'status' : 'ok', 'html': rendered }
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')
    else:
        if (type == 'quote'):
            context = {'form': form}
        else:
            context = {'messageform': form}
        context.update(csrf(request))
        rendered = render_to_string(template_names[type], context)
        json = { 'status' : 'error', 'html': rendered }
        return HttpResponse(simplejson.dumps(json), mimetype='application/json')