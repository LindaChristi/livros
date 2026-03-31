from django.http import JsonResponse
from .models import Livro

def listar_livros(request):
    return JsonResponse(list(Livro.objects.all().values()), safe=False)

def livros_lidos(request):
    return JsonResponse(list(Livro.objects.filter(status='LIDO').values()), safe=False)