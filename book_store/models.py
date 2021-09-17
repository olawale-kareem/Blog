from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify



class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'


class Address(models.Model):
    street= models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street} {self.postal_code} {self.city}'
    
    class Meta:
        verbose_name_plural = 'Address'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='author', null=True)

    def full_name(self):
        return  f' {self.first_name} {self.last_name} '

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Author'


class Books(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default='',blank=True, null=False, db_index=True) #db_index makes serching this field more efficient with our querries
    published_countries = models.ManyToManyField(Country) # note u don't set-up an 'on-delete=models.CASCADE' for this property.


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

    class Meta:
        verbose_name_plural = 'Books'