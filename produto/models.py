from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    data_criacao = models.DateTimeField(default=timezone.now),
    valor_total = models.DecimalField(decimal_places=2, max_digits=10)
    ativo = models.BooleanField(default=True)

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    qtd_estoque = models.IntegerField()
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=10)
    imagem = models.TextField()
    ativo = models.BooleanField(default=True)  

class PedidoItem(models.Model):
    qtd = models.FloatField()
    desconto = models.FloatField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido =models.ForeignKey(Pedido, on_delete=models.CASCADE)

    


