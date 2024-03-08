from django.contrib import admin
from .models import barcold
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','note','price','status')
    search_fields = ('name','note','price','status')
admin.site.register(barcold,MenuAdmin)