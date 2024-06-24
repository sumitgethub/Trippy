from django.contrib import admin
from Account.models import Role, User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number','otp','email','email_verification')
    list_display_links = ('id', 'phone_number','otp','email','email_verification')
    search_fields = ('id', 'phone_number','otp','email','email_verification')

class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'overview', 'cost')
    list_filter = ('name',)
    search_fields = ('name', 'overview')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_filter = ('name',)
    search_fields = ('name', 'address')

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'image')
    list_filter = ('package',)
    search_fields = ('package__name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'user', 'rating', 'comment')
    list_filter = ('package',)
    search_fields = ('package__name', 'user__username')

admin.site.register(User,UserAdmin)
admin.site.register(Role)