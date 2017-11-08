from .models import Recipe
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for owners that allows recipes to be viewed or edited
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        return self.request.user.recipes.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FeedRecipeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing all recipes
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
