from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    search_fields = ('nome','email','idade')
