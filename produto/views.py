from django.shortcuts import render
from produto.models import Produto

# Create your views here.


def index(request):
    lista_produto = Produto.objects.all()

    return render(request, 'produto/index.html', {'lista_produto':lista_produto})


def add(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome_produto =  request.POST.get('nome', None)
        produto.qtd_estoque =  request.POST.get('qtd', None)
        produto.preco_unitario =  request.POST.get('preco', None)
        produto.ativo =  request.POST.get('ativo', None)
        produto.imagem = request.POST.get('imagem', None)
        produto.save()
        lista_produto = Produto.objects.all()
    return render(request, "produto/resposta.html", context={'lista_produto':lista_produto})

def busca(request):
    if request.method == "GET":
        srch = request.GET.get('src', None)
        if srch:
            produtos = Produto.objects.filter(nome=srch)
        else:
            produtos = Produto.objects.all()
    return render(request, "resultado_busca.html", context={'lista_produto':lista_produto})