from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True )
    # deleted = models.BooleanField(default=0)
    # def __str__(self):
    #     return self.name
