from django.db import models
from common.models import CommonModel

# Create your models here.
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)