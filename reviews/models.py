from django.db import models

class Reviews(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.user_name