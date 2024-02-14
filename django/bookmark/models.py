from django.db import models

# Create your models here.

class bookmark(models.Model):
    title = models.CharField("제목", max_length=64)
    link = models.URLField("링크")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "북마크"
        verbose_name_plural = "북마크  목록"