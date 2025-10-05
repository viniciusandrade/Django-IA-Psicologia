from django.contrib import admin
from .models import  Gravacoes, Pergunta, DataTreinamento

# Register your models here.
admin.site.register(Gravacoes)
admin.site.register(Pergunta)
admin.site.register(DataTreinamento)
