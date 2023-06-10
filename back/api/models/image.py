from django.db import models


class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", null=False)
    class Meta:
        db_table = "image"