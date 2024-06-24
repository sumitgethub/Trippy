from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .utils import get_custom_jwt_token
from .serializers import RoleSerializer, UserSerializer
from django.utils.crypto import get_random_string
from .models import Role, User
from django.shortcuts import get_object_or_404

from django.db import transaction


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

@api_view(['POST'])
def user_login_or_register(request):
    if request.method == "POST":
        phone_number = request.data.get("phone_number")
        otp = request.data.get("otp")

        if not phone_number:
            return Response(
                {"error": "phone_number field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Check if the user exists with the provided phone number
            user = User.objects.get(phone_number=phone_number)

            if otp:
                # If OTP is provided, perform login process
                if int(user.otp) != int(otp):
                    return Response(
                        {"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST
                    )

                # Generate access and refresh tokens for the user
                refresh = get_custom_jwt_token(user)
                access_token = refresh["access"]
                refresh_token = refresh["refresh"]

                user.phone_number_verification = True
                user.save()

                response = Response(
                    {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                        "msg": "Login successful",
                    },
                    status=status.HTTP_200_OK,
                )
                # Set 'access_token' cookie
                response.set_cookie(
                    "access_token", access_token, httponly=True, samesite="strict"
                )

                # Set 'refresh_token' cookie
                response.set_cookie(
                    "refresh_token", refresh_token, httponly=True, samesite="strict"
                )
                return response

            # If OTP is not provided, resend the generated OTP for login
            otp = get_random_string(length=4, allowed_chars="0123456789")
            user.otp = otp
            # user.otp = 1234
            user.save()

            return Response(
                {"msg": f"OTP: {otp}. Please verify your phone number."},
                status=status.HTTP_200_OK,
            )

        except User.DoesNotExist:
            # If the user does not exist, check if OTP is provided
            if otp:
                return Response(
                    {"error": "Phone number not registered. Please register first."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            # If the user does not exist, create a new user with the provided data
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                with transaction.atomic():
                    otp = get_random_string(length=4, allowed_chars="0123456789")
                    serializer.save(otp=otp)

                    # Return a success response with the generated OTP
                    return Response(
                        {"msg": f"OTP: {otp}. Please verify your phone number."},
                        status=status.HTTP_200_OK,
                    )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED
    )



class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
    

@api_view(['GET'])
def check_phone_number(request):
    phone_number = request.GET.get('phone_number', None)
    if phone_number:
        exists = User.objects.filter(phone_number=phone_number).exists()
        return Response({'exists': exists})
    else:
        return Response({'error': 'Phone number not provided'}, status=status.HTTP_400_BAD_REQUEST)