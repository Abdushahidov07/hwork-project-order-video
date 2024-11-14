from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.category_name
    

class City(models.Model):
    city_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.city_name

class Region(models.Model):
    region_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.region_name

class Street(models.Model):
    street_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.street_name
    
class Teatre(models.Model):
    name_teatre = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street,  on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_teatre
    

class Films(models.Model):
    title = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    descriptions = models.TextField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    tikets = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    teatre = models.ForeignKey(Teatre,  on_delete=models.CASCADE)
    video = models.FileField(upload_to="static/videos", max_length=100)
    img = models.ImageField(upload_to="static/images", height_field=None, width_field=None, max_length=None)
    date_view = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    class Meta:
        default_permissions = ('add', 'change', 'delete') 
        permissions = (
            ('viev_film', 'Can view film'),
        )

    def __str__(self):
        return self.title


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE) 
    qvantity = models.IntegerField()
    PAY = (
        ('card', 'Card'),
        ('cash', 'cash')
    )
    type_pay = models.CharField(max_length=100,choices=PAY)
    def __str__(self):
        return f"Order: {self.id}"
    