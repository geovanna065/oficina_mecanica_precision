from django import forms
from .models import Item, Movimentacao

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'codigo', 'localizacao', 'quantidade', 'estoque_minimo', 'descricao']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['item', 'tipo', 'quantidade', 'observacao']