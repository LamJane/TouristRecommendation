from django.contrib import admin

# Register your models here.

from TRlogin.models import User

admin.site.register([User])