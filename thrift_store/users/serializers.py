from rest_framework import serializers
from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            # 'password',
            'contact_no',
            'location',
            # 'products_listed'
            # 'wishlist'
            # 'cart'
            'date_joined',
            'is_staff',
        )
