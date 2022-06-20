# db/models.py
from django.db import models
from manage import init_django

init_django()


class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
