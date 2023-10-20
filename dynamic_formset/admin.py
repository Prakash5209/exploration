from django.contrib import admin

from dynamic_formset.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","title",)