from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_captcha(value):
    if value != 18:
        raise ValidationError(u'Wrong answer to the tricky question!')
    pass

class QuoteRequest(models.Model):
    name = models.CharField("Your name", max_length=128, blank=False)
    #lastname = models.CharField("Last name", editable=False, max_length=128, blank=False)
    email = models.EmailField("Email address", blank=False)
    company = models.CharField("Company name", max_length=128, blank=True, null=True)
    phone = models.CharField("Phone number", max_length=32, blank=True, null=True)
    captcha = models.CharField("Tricky question, multiply 9 by 2 please", max_length=32, blank=False, null=False, validators=[validate_captcha])
    message = models.TextField(max_length=16536, blank=False)
    sent_to = models.ManyToManyField(User, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    def __unicode__(self):
        return self.name + ', ' + self.email
