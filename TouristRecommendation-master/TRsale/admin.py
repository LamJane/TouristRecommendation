from django.contrib import admin

# Register your models here.

from TRsale.models import DmSale,DmFree,DmShanghai,DmYunnan,DmXinjiang,DmGuangdong,All

admin.site.register([DmSale,DmFree,DmShanghai,DmYunnan,DmXinjiang,DmGuangdong,All])