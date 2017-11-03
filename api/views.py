from .models import Recipe
from rest_framework import viewsets
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
