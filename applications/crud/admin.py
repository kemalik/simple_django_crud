from django.contrib import admin

from applications.crud.models import Cars

class Cars_Admin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year']

admin.site.register(Cars, Cars_Admin)
