from django.contrib import admin
from learning_logs.models import Topic
from learning_logs.models import Entry

admin.site.register(Topic) #Registrando um modelo para o painel administrativo 
admin.site.register(Entry)