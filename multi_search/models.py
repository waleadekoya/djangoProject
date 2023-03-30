from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Name(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
