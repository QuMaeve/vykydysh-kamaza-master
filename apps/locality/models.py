from django.db import models

# Create your models here.
class Locality(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name = "Район" )
    deleted = models.BooleanField(default=0)
    
    def __str__(self):
        return self.name
    class Meta:
         verbose_name = "Район"
         verbose_name_plural = "Район"