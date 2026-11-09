from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """
    Página principal do learning_logs
    """
    return render(request, 'learning_logs/index.html')

def sobre(request):
    """
    Pagina sobre do learning_logs
    """
    return render(request, 'learning_logs/sobre.html')

def topics(request):
    """
    Mostra todos os assuntos.
    """
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topic }
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """
    Mostra todas as entradas de cada topico
    """
    #Busca um topico com o mesmo id
    topic = Topic.objects.get(id = topic_id)
    #Busca todas as entreis relacionadas ao tópico em questão
    entries = topic.entry_set.order_by('-date_added')#O - faz com que seja na ordem inversa
    context = {'topics':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)
