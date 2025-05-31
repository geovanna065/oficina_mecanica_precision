from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Movimentacao
from .forms import ItemForm, MovimentacaoForm

def dashboard(request):
    itens = Item.objects.all()
    return render(request, 'controle/dashboard.html', {'itens': itens})

def novo_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'controle/item_form.html', {'form': form})

def editar_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'controle/item_form.html', {'form': form})

def movimentacao(request):
    form = MovimentacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'controle/movimentacao_form.html', {'form': form})