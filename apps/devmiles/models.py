from django.db import models
from django.contrib.auth.models import User

class QuoteRequest(models.Model):
    name = models.CharField("Your name", max_length=128, blank=False)
    #lastname = models.CharField("Last name", editable=False, max_length=128, blank=False)
    email = models.EmailField("Email address", blank=False)
    company = models.CharField("Company name", max_length=128, blank=True, null=True)
    phone = models.CharField("Phone number", max_length=32, blank=True, null=True)
    message = models.TextField(max_length=16536, blank=False)
    sent_to = models.ManyToManyField(User, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    def __unicode__(self):
        return self.name + ', ' + self.email
