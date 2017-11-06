from .models import Recipe
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
