from django.contrib import admin
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'js/custom.js',
        )

admin.site.register(Message, MessageAdmin)