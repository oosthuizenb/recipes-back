from .models import Recipe, Image
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import RecipeSerializer, ImageSerializer

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

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def image_list(request):
    """
    List all the user's images or create a new image
    """
    if request.method == 'GET':
        images = Image.objects.filter(owner=request.user)
        serializer = ImageSerializer(images)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, IsOwnerOrReadOnly))
def image_detail(request, pk):
    """
    Retrieve, update or delete an image.
    """
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data)
    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
