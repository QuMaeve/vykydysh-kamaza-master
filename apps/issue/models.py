from django.db import models

# Create your models here.
class Issue(models.Model):
    user = models.ForeignKey(
        'user.CustomUser',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='issue_user',
    )
    book = models.ForeignKey(
        'book.Book',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='issue_book',
    )
    start_time = models.DateField(
        # editable=True,
        auto_now_add=True, 
        blank=True)

    day_count = models.IntegerField(null=True, blank=True)
    end_time = models.DateField(
        null=True,
        blank=True)
    # deleted = models.BooleanField(default=0)

    class Meta:
         verbose_name_plural = "Выдача"
         verbose_name_plural = "Выдачи"
    # def __str__(self):
    #     return self.name
