# accounts/serializers.py
from rest_framework import serializers
from .models import CMSUser

class CMSUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CMSUser
        # Fields that can be set by regular users
        fields = ['phone_number', 'full_name', 'role', 'date_of_birth', 'is_active', 'is_staff', 'password']
        # Fields that cannot be set by regular users, but can be set by admins
        read_only_fields = ['is_active', 'is_staff']  
    def create(self, validated_data):
        """
        Ensure that new users are always created as non-staff, non-superuser.
        """
        password = validated_data.pop('password')
        user = CMSUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Prevent users from updating 'is_active' or 'is_staff' via API.
        """
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
