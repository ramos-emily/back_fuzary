from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *

class SpellSPIView(views.APIView):
    
    #POST cadastra dados na API
    def post(self, request):
        
        #armazenar os dados em JSON
        spellJson = request.data 
        
        #transformar JSON em python
        spellSerialized = SepllsSerializer(data=spellJson)
        
        #verificar se os dados estao corretos
        spellSerialized.is_valid(raise_exception=True)
        
        #salvar no banco
        spellSerialized.save()
        
        #retornar pro cliente resutado da requisição
        return Response(status=201, data=spellSerialized.data)