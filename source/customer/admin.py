from django.contrib import admin

# Register your models here.
from .models import Generator, Prequal, Manifest


admin.site.register(Generator)
admin.site.register(Prequal)
admin.site.register(Manifest)
