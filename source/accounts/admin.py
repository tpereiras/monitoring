from django.contrib import admin

# Register your models here.
from .models import Activation, Company


admin.site.register(Activation)
admin.site.register(Company)
