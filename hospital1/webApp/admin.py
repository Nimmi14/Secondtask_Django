from django.contrib import admin
from .models import User, Patient,Doctor,Blog
# Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)


@admin.register(Blog)
class blogAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'title']