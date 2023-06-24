from django.contrib import admin
from .models import Cat, User


class CatAdmin(admin.ModelAdmin):
    list_display = ('abb', 'name', 'temperament', 'description', 'wikipedia_url',)
    list_editable = ('name',)
    list_filter = ('abb', 'name',)


admin.site.register(Cat, CatAdmin)
admin.site.register(User)