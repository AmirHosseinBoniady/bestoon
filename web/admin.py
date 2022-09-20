from sre_constants import IN
from django.contrib import admin
from .models import Expence, Income

# Register your models here.
admin.site.register(Expence)
admin.site.register(Income)
