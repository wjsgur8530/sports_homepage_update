from django.contrib import admin

# Register your models here.
from reference.models import Material, Photo

admin.site.register(Material)
admin.site.register(Photo)