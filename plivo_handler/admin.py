from django.contrib import admin

# Register your models here.
from .models import Numbers, Messages
admin.site.register(Messages)
admin.site.register(Numbers)