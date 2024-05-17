from django.contrib import admin

from .models import Quote, Author, Tag
# Register your models here.

admin.site.register([Quote,Author,Tag])


