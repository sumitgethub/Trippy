# from django.shortcuts import render

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from django.http import Http404
# from Bookings.models import Booking, Hotel, ImageGallery, Package, Review
# from Bookings.serializers import BookingSerializer, HotelSerializer, ImageGallerySerializer, PackageSerializer, ReviewSerializer


# class PackageListCreate(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         packages = Package.objects.all().prefetch_related('reviews', 'images', 'hotels')
#         serializer = PackageSerializer(packages, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = PackageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PackageDetail(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Package.objects.prefetch_related('reviews', 'images', 'hotels').get(pk=pk)
#         except Package.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         package = self.get_object(pk)
#         serializer = PackageSerializer(package)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         package = self.get_object(pk)
#         serializer = PackageSerializer(package, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         package = self.get_object(pk)
#         package.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class HotelListCreate(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         hotels = Hotel.objects.all()
#         serializer = HotelSerializer(hotels, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = HotelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class ImageGalleryListCreate(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, format=None):
#         images = ImageGallery.objects.all()
#         serializer = ImageGallerySerializer(images, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ImageGallerySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ReviewListCreate(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# class BookingListCreate(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         bookings = Booking.objects.all()
#         serializer = BookingSerializer(bookings, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookingDetail(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Booking.objects.get(pk=pk)
#         except Booking.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         serializer = BookingSerializer(booking)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         serializer = BookingSerializer(booking, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         booking = self.get_object(pk)
#         booking.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from Bookings.models import Package, Hotel, ImageGallery, Review, Booking
from Bookings.serializers import PackageSerializer, HotelSerializer, ImageGallerySerializer, PackageSerializer2, ReviewSerializer, BookingSerializer
from Account.permissions import CanRetrieveAdminAPI, IsAdminUser,IsCustomerUser
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

class PackageListCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser | CanRetrieveAdminAPI]

    def get(self, request):
        packages = Package.objects.all().prefetch_related('reviews', 'images', 'hotels')
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

    def post(self, request ,format=None):
        serializer = PackageSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PackageDetail(APIView):
    permission_classes = [IsAuthenticated,IsAdminUser | CanRetrieveAdminAPI]

    def get_object(self, pk):
        try:
            return Package.objects.prefetch_related('reviews', 'images', 'hotels').get(pk=pk)
        except Package.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        package = self.get_object(pk)
        serializer = PackageSerializer(package)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        package = self.get_object(pk)
        serializer = PackageSerializer(package, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        package = self.get_object(pk)
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HotelListCreate(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser | CanRetrieveAdminAPI]

    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageGalleryListCreate(APIView):
    
    permission_classes = [IsAuthenticated, IsAdminUser | CanRetrieveAdminAPI]

    
    def get(self, request, format=None):
        images = ImageGallery.objects.all()
        serializer = ImageGallerySerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImageGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewListCreate(APIView):
    permission_classes = [IsAuthenticated, IsCustomerUser | CanRetrieveAdminAPI]

    def post(self, request, format=None):
        request.data['user'] = request.user.id
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingListCreate(APIView):
    permission_classes = [IsAuthenticated, IsCustomerUser | CanRetrieveAdminAPI]

    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['user'] = request.user.id
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingDetail(APIView):
    permission_classes = [IsAuthenticated, IsCustomerUser |CanRetrieveAdminAPI]

    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)