#transformar python em json e vice verse
from rest_framework import serializers
from .models import * #o ponto é pra dizer q é nosso nao uma bibilhoteca e o asteristico pra pegar tudo

class SepllsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        many = True
        fields = '__all__' 
        
        
        #repetir isso com as coisas la de nome, feitiço, casa...