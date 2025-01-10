from django.urls import path #path é o caminho pra direcionar ate a views
from .views import *


urlpatterns = [
    path('spells/', SpellSPIView.as_view(), name="spell")
]