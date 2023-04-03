from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(
        'author.Author',
        null=True,
        on_delete=models.SET_NULL,
        related_name='book_author',
    )
    genre = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(null=False, blank=True, default=1000)
    description =  models.TextField(max_length=500, null=True, blank=True)
    doc_path = models.FileField(upload_to="documents/", null=True, blank=True)
    doc_url = models.CharField(max_length=2048 , null=True, blank=True)
    cover_path = models.FileField(upload_to="documents/", null=True, blank=True)
    cover_url = models.CharField(max_length=2048 , null=True, blank=True)

    user_id = models.ForeignKey(
        'user.CustomUser',
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
        related_name='book_user',
    )
    deleted = models.BooleanField(default=0)
    def __str__(self):
    #     self.name = name
    #     self.genre = genre
    #     self.author = author
        return  f"{self.author} - {self.name} "
    class Meta:
         verbose_name = "Книга"
         verbose_name_plural = "Книги"