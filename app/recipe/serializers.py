from core.models import Tag

from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for  Tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_field = ('id',)
