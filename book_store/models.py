from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Books(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(max_length=100, null=True)
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default='',blank=True, null=False, db_index=True) #db_index makes serching this field more efficient with our querries

    # use this in the template needed, the href should call the get_absolute_url

    # use with id
    # def get_absolute_url(self):
    #     return reverse("book-detail", args=[self.id])

    # use with slug
    # def get_absolute_url(self):
    #     return reverse("book-detail", args=[self.slug])

    # overiding the save method to allow for slug
    # don't need this method no more as long as the admin predefined field is taking care of this
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title} {self.rating}' 