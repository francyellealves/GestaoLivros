import stat
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets, status, fields
from rest_framework.response import Response
from .models import Autor, Livro
from .serializers import AutorSerializer, LivroSerializer
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions
from django.utils import timezone
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Livro
from .serializers import LivroSerializer
from django.db.models import Count

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

    def create(self, request, *args, **kwargs):
        if Autor.objects.filter(nome=request.data.get('nome')).exists():
            return response({"detail": "Autor já existe"},
status=stat.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo','autor_nome']

@action(detail=True, methods=['patch'])
def atualizar_titulo(self, request, pk=None):
    livro = self.get_object()
    livro.titulo = request.data.get('titulo')
    livro.save()
    return response({'status': 'Título atualizado!'})

class LivrosUltimoAnoView(APIView):
    def get(self, request):
        ultimo_ano = timezone.now() - timedelta(days=365)
        livros = Livro.objects.filter(data_publicacao__gte=ultimo_ano)
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    
class LivrosEstatisticasView(APIView):
    def get(self, request):
        total_livros = Livro.objects.count()
        livros_por_autor = Livro.objects.values('autor__nome').annotate(total=Count('id'))
        data = {
            'total_livros': total_livros,
            'livros_por_autor': livros_por_autor,
        }
        return Response(data)
    
