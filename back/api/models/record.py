from django.db import models


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "record"