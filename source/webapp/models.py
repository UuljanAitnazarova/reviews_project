from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Product(models.Model):

    CATEGORY_CHOICE = [
        ('bags', 'Bags'),
        ('shoes', 'Shoes'),
        ('glasses', 'Glasses'),
        ('scarves', 'Scarves'),
        ('gloves', 'Gloves')
    ]


    name = models.CharField(max_length=150, blank=False, null=False)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='pictures')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='review', on_delete=models.CASCADE)
    product = models.ForeignKey('webapp.Product', related_name='review', on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=False, null=False)
    grade = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], blank=False, null=False)
    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


