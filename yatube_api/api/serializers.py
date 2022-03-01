from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Group, Follow, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def create(self, validated_data):
        follow = Follow.objects.create(
            user=validated_data.get('user'),
            following=validated_data.get('following'))
        return follow

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise serializers.ValidationError('selfsubscribe is denied')
        return attrs
