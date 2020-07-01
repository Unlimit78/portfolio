from django.contrib import admin

# Register your models here.
from .models import Attachments,Mail

admin.site.register(Attachments)
admin.site.register(Mail)