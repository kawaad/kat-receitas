from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):

    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete',
        4: 'Bolo de chocolate',
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(response, 'index.html', dados)


def receita(response):
    return render(response, 'receita.html')
