from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer()
    class Meta:
        model = Feed
        fields = '__all__'
        depth = 1