from django.contrib import admin
from .models import Profile, Business, Neighbourhood, Alerts

# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Alerts)