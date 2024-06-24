from django.urls import path
from .views import (
    BookingListCreate,
    PackageListCreate,
    PackageDetail,
    HotelListCreate,
    ImageGalleryListCreate,
    ReviewListCreate
)

urlpatterns = [
    path('packages/', PackageListCreate.as_view(), name='package-list-create'),
    path('packages/<int:pk>/', PackageDetail.as_view(), name='package-detail'),
    path('hotels/', HotelListCreate.as_view(), name='hotel-list-create'),
    path('images/', ImageGalleryListCreate.as_view(), name='image-gallery-list-create'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('Booking/', BookingListCreate.as_view(), name='Booking-list-create'),
]
