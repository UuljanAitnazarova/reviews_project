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
