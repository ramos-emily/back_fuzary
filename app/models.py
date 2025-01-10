from django.db import models

# Create your models here.

class Spell(models.Model): #vai se comportar como models, la da tabela Spell
    name = models.CharField(max_length=200) #char é limitado
    description = models.TextField() #pode ser qualquer tamanho sem limitação
    
    def __str__(self):
        return self.name
    
class House(models.Model):
    name = models.CharField(max_length=100, default='Desconhecida')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Characters(models.Model):
    name = models.CharField(max_length=100, default='Desconhecida')
    house = models.ForeignKey(House, verbose_name="Character's house", on_delete=models.CASCADE)
    wizard = models.BooleanField(default=True)
    species = models.CharField(max_length=100, default='Desconhecida')
    eyecolors = models.CharField(max_length=100, default='Desconhecida')
    haircolor = models.CharField(max_length=100, default='Desconhecida')
    img = models.TextField()
    created = models.DateField(editable=False, auto_now=True)
    
    
    def __str__(self):
        return self.name


    #name "name": "Harry Potter"
    #house "house": "Gryffindor",
    #wizard 	"wizard": true, boolean
    #species  "species": "human",
    #eyecolor "eyeColour": "green",
    #haircolor "hairColour": "black"
    #actor 	"actor": "Daniel Radcliffe",
    #img (TEXTFIELD -> link da web)
    