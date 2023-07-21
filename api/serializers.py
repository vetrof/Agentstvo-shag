from rest_framework import serializers

from homes.models import Home


class HomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = [
            'id',
            'title',
            'info',
            's',
            'district',
            'cost',
            'img',
            'manager',
            'category'
        ]
