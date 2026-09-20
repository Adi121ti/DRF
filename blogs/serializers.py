from .models import Comment, Blog
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ="__all__"
        
        
class BlogSerializer(serializers.ModelSerializer):
    #related_name is used over here
    comments = CommentSerializer(many=True, read_only = True)
    class Meta:
        model = Blog
        fields ="__all__"