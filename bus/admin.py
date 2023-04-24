# Register your models here.
from django.contrib import admin
from .models import Bus, City, Route, Trip, Ticket

admin.site.register(Bus)
admin.site.register(City)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(Ticket)
