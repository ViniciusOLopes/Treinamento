from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

@login_required #decorator que faz com que so seja acessado se estiver logado
def topics(request):
    """
    Mostra todos os assuntos.
    """
    topic = Topic.objects.filter(owner= request.user).order_by('date_added')
    context = {'topics': topic }
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """
    Mostra todas as entradas de cada topico
    """
    #Busca um topico com o mesmo id
    topic = Topic.objects.get(id = topic_id)
    #Garante que o topico pertence a quem faz a requisisção
    if topic.owner != request.user:
        raise Http404

    #Busca todas as entreis relacionadas ao tópico em questão
    entries = topic.entry_set.order_by('-date_added')#" - " faz com que seja na ordem inversa
    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

@login_required
def add_topic(request):
    """
    Adiciona um novo tópico
    """
    if request.method != 'POST':
        # Caso nenhum dado seja submetído irá criar um formulário em branco (Irá renderizar o formulário)
        form = TopicForm()
    else:
        # Caso dados sejam submetídos, processará os dados
        form = TopicForm(request.POST) #O form recebe o formulário com os valores

        if form.is_valid():#Verifica se todos os valores estão preenchidos corretamentes
            
            #Cria um novo topic mas o atribui o owner do topico ao usuário
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics')) #Vai redirecionar de volta para a pagina topics
    
    context = {'form': form}
    return render(request, 'learning_logs/add_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    """
    Editar um Tópico que já existe
    """
    topic = Topic.objects.get(id = topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TopicForm(instance=topic)

    else:
        #Pegando dados pelo POST e submetendo eles
        form = TopicForm(instance=topic, data=request.POST)

        #Validando dados
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_topic.html', context)

@login_required
def add_entry(request, topic_id):
    """
    Adiciona um novo entry
    """
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Caso nenhum dado seja submetído irá criar um formulário em branco (Irá renderizar o formulário)
        form = EntryForm()

    else:
        # Caso dados sejam submetídos, processará os dados
        form = EntryForm(data=request.POST) #O form recebe o formulário com os valores
        
        #Verifica se todos os valores estão preenchidos corretamentes
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            
            return HttpResponseRedirect(reverse('topic', args=[topic_id])) #Vai redirecionar de volta para a pagina topics

    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/add_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """
    Edita uma entrada existente
    """
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Preenche previamente o form que sera aberto
        form = EntryForm(instance=entry)

    else:
        #Submetendo dados do POST para o forms
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}

    return render(request,'learning_logs/edit_entry.html',context)