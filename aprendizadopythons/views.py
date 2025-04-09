from django.shortcuts import render, get_object_or_404
from .models import Topico, Entrada
from .forms import Topico_form, Entrada_form
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Funcao para retornar a pagina principal do app aprendizadopythons"""
    return render(request,'aprendizadopythons/index.html')

def topicos(request):
    """Mostra todos os assuntos"""
    topicos = Topico.objects.order_by('date_added')
    contexto = {'topicos' : topicos}
    return render(request,'aprendizadopythons/topicos.html', contexto)
    #render x redirect : render é para renderizar

def topico(request, topico_id):

    topico = Topico.objects.get(id = topico_id)
    entradas = topico.entrada_set.order_by('-date_added')
    contexto = {'topico': topico, 'entradas': entradas}
    return render(request,'aprendizadopythons/topico.html', contexto)

def novo_topico(request):
    if request.method != 'POST':
        #Nenhum dado submetido. Cria um formulario em branco
        form = Topico_form()
    else:
        # Dados de POST submetidos. processa os dados
        form = Topico_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topicos'))
        #cria uma redirecionamento para uma url especifica que já foi renderizada
        #reverse gera uma URL a partir da configuracao do nome da URL
    
    contexto = {'form': form}
    return render(request, 'aprendizadopythons/novo_topico.html', contexto)


def nova_anotacao(request, topico_id):
    topico = Topico.objects.get(id = topico_id)

    if request.method != 'POST':
        form = Entrada_form()

    else:
        form = Entrada_form(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.topico = topico
            nova_entrada.save()
            return HttpResponseRedirect(reverse('topico', args=[topico_id]))

    contexto = {'topico': topico, 'form': form}

    return render(request, 'aprendizadopythons/nova_anotacao.html', contexto)

def edit_entrada(request, entrada_id):
    entrada = Entrada.objects.get(id=entrada_id)
    topico = entrada.topico

    if request.method != 'POST':
        form = Entrada_form(instance=entrada)

    else:
        form = Entrada_form(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topico', args=[topico.id]))
        
    contexto = {'entrada': entrada, 'topico': topico, 'form': form}

    return render(request, 'aprendizadopythons/edit_entrada.html', contexto)

def delete_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk = entrada_id)
    topico = entrada.topico
    entrada.delete()
    return HttpResponseRedirect(reverse('topico', args=[topico.id]))



  
