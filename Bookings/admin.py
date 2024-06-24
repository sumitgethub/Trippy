from django.contrib import admin

from Bookings.models import Hotel, ImageGallery, Package, Review

# Register your models here.
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'overview', 'cost')
    list_filter = ('name',)
    search_fields = ('name', 'overview')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_filter = ('name',)
    search_fields = ('name', 'address')

@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'image')
    list_filter = ('package',)
    search_fields = ('package__name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'user', 'rating', 'comment')
    list_filter = ('package',)
    # search_fields = ('package__name', 'user__username')