from django.contrib import admin
from  .models import *
# Register your models here.

@admin.register(Manager)
class ViewAdmin(admin.ModelAdmin):
  pass


