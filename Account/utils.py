from rest_framework_simplejwt.tokens import RefreshToken




def get_custom_jwt_token(user):
    refresh = RefreshToken.for_user(user)

    # Add common claims to the token
    refresh['phone_number'] = user.phone_number
    refresh['is_active'] = user.is_active
    refresh['phone_number_verification'] = user.phone_number_verification
    refresh['role_id'] = user.role.id if user.role else None
    refresh['role_name'] = user.role.name if user.role else None
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
