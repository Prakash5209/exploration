from django.contrib import admin

from demo.models import DemoModel

@admin.register(DemoModel)
class DemoModelAdmin(admin.ModelAdmin):
    list_display = ("name","title")