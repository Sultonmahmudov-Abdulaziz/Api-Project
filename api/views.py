from django.shortcuts import render
from .models import Card
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CardSerializer
from django.shortcuts import get_object_or_404



class CardApiView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)   
        return Response(serializer.data)
    

class OneCardApiView(APIView):
    def post(self, request):
        if "card_number" not in request.data:
            data = {
                "status": False,
                "message": "card_number is required"

            }

            return Response(data)
        

        card_number = request.data["card_number"]
        card = get_object_or_404(Card, card_number=card_number)

    
        serializer = CardSerializer(card)
        return Response(serializer.data)
    


