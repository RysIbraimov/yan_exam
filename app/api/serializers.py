from rest_framework import serializers
from .models import Post,Comment,GradePost

class PostSerializer(serializers.ModelSerializer):
    average_rate = serializers.ReadOnlyField(source='get_average_grade')
    class Meta:
        model = Post
        fields = ['text','average_rate']
        read_only_fields = ['created_at','author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at','post','author']

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            comment = Comment.objects.create(text=validated_data['text'],
                                             author=validated_data['author'],
                                             post=validated_data['post'])
            return comment
        else:
            return Comment.objects.create(text=validated_data['text'],
                                        comment_author=validated_data['comment_author'],
                                        post=validated_data['post'])



class PostRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradePost
        fields = '__all__'
        read_only_fields = ['author','post']




