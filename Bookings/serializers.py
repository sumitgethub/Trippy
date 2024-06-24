from rest_framework import serializers
from .models import Booking, Package, Hotel, ImageGallery, Review

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address']

class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = ['id', 'package', 'image']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'package', 'user', 'rating', 'comment']

class PackageSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    images = ImageGallerySerializer(many=True, read_only=True)
    hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = ['id', 'name', 'overview', 'cost', 'reviews', 'images', 'hotels']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'package', 'start_date', 'end_date']
        
class PackageSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Package
        fields = '__all__'