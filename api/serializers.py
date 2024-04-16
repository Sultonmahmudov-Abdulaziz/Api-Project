from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:Card
    fields = ('id', 'card_number', 'valid_time', 'card_type', 'bank_name', 'name', 'user')