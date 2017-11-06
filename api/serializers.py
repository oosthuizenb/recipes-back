from .models import Recipe
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Recipe
        fields = ('id', 'owner', 'title', 'serves', 'ingredients', 'method')
