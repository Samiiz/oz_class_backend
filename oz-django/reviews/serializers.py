from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import FeedUserSerializer

class ReviewSerializer(ModelSerializer):
     user = FeedUserSerializer()

     class Meta:
          model = Review
          fields = '__all__'