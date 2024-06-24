from django.db import models

from Account.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

class Package(models.Model):
    name = models.CharField(max_length=255)
    overview = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    hotels = models.ManyToManyField(Hotel, related_name='packages')

class Review(models.Model):
    package = models.ForeignKey(Package, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

class ImageGallery(models.Model):
    package = models.ForeignKey(Package, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='packages/')



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
