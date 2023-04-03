from django.db import models

# Create your models here.
class Establishment(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True,verbose_name = "Учебное учреждение")
    contacts = models.TextField(max_length=1000, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    requisites =  models.TextField(max_length=1000, null=True, blank=True)
    locality = models.ForeignKey(
        'locality.Locality',
        null=True,
        on_delete=models.SET_NULL,
        related_name='establishment_locality',
    )
    deleted = models.BooleanField(default=0)
    def __str__(self):
        return self.name
    class Meta:
         verbose_name = "Учебное учреждение"
         verbose_name_plural = "Учебное учреждение"
