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
    return render(request, "produto/form.html")


def busca(request):
    if request.method == "GET":
        busca = request.GET.get('buscar', None)
        if busca:
            produtos = Produto.objects.filter(nome=)