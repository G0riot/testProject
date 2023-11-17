from django.contrib import admin
from .models import Questionary


# Register your models here.
class QuestionaryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'use', 'text']
    list_editable = ['use']


admin.site.register(Questionary, QuestionaryAdmin)
