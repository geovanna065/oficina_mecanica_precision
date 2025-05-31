from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    localizacao = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=1)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

    def em_alerta(self):
        return self.quantidade <= self.estoque_minimo


class Movimentacao(models.Model):
    TIPOS = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPOS)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.tipo == 'entrada':
            self.item.quantidade += self.quantidade
        elif self.tipo == 'saida':
            self.item.quantidade -= self.quantidade
        self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo.title()} - {self.item.nome} ({self.quantidade})"