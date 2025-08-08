from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inscricao
from .forms import InscricaoForm

@login_required
def listar_inscricoes(request):
    inscricoes = Inscricao.objects.filter(membro=request.user)
    return render(request, 'inscricoes/listar_inscricoes.html', {'inscricoes': inscricoes})

@login_required
def criar_inscricao(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.membro = request.user
            inscricao.save()
            return redirect('listar_inscricoes')
    else:
        form = InscricaoForm()
    return render(request, 'inscricoes/criar_inscricao.html', {'form': form})

@login_required
def editar_inscricao(request, id):
    inscricao = Inscricao.objects.get(id=id)
    if request.method == 'POST':
        form = InscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            return redirect('listar_inscricoes')
    else:
        form = InscricaoForm(instance=inscricao)
    return render(request, 'inscricoes/editar_inscricao.html', {'form': form})

@login_required
def excluir_inscricao(request, id):
    inscricao = Inscricao.objects.get(id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('listar_inscricoes')
    return render(request, 'inscricoes/excluir_inscricao.html', {'inscricao': inscricao})