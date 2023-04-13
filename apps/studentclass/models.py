from django.db import models

# Create your models here.
class Class(models.Model):
    number = models.IntegerField(null=True, blank=True )
    literature = models.CharField(max_length=10, null=True, blank=True)
    establishment = models.ForeignKey(
        'establishment.Establishment',
        null=True,
        on_delete=models.SET_NULL,
        related_name='class_establishment',
        verbose_name= "Школа"
    )
    # deleted = models.BooleanField(default=0)
    def __str__(self):
    #     self.name = name
    #     self.genre = genre
    #     self.author = author
        return  f"{self.establishment} - {self.number}{self.literature} "
    class Meta:
         verbose_name= "Класс"
         verbose_name_plural = "Класс"