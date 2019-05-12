from django.contrib import admin
from buyers.models import Buyer, BuyLog

# Register your models here.

admin.site.register(Buyer)
admin.site.register(BuyLog)
