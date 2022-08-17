from email.policy import default
from pygments import highlight
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



# class SnippetSerializer(serializers.Serializer):
    # """
    # Long-road/custom approach implementing serializers
    # """
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """Create new instance of a Snippet"""
#         return Snippet.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         """Update instance of an existing Snippet"""
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """ Model serializer, default implementation for create() and update() methods """
    
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    
    #example to hyperlink fields
    #linenos = serializers.HyperlinkedIdentityField(view_name='snippet-linenos', format='html' )

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 
                  'title','code','linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id','username' ,'snippets']


