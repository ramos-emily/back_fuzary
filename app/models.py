from django.db import models

# Create your models here.

class Spell(models.Model): #vai se comportar como models, la da tabela Spell
    name = models.CharField(max_length=200) #char é limitado
    description = models.TextField() #pode ser qualquer tamanho sem limitação
    
    def __str__(self):
        return self.name
    
class Characteres(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    wizard = models.BooleanField(True)
    species = models.CharField(max_length=100)
    eyecolors = models.CharField(max_length=100)
    haircolor = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    img = models.TextField("https://pbs.twimg.com/profile_images/1083038156436525057/oc7dOkJw_400x400.jpg", blank=True, null=True)


    #name "name": "Harry Potter"
    #house "house": "Gryffindor",
    #wizard 	"wizard": true, boolean
    #species  "species": "human",
    #eyecolor "eyeColour": "green",
    #haircolor "hairColour": "black"
    #actor 	"actor": "Daniel Radcliffe",
    #img (TEXTFIELD -> link da web)
    