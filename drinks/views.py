from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_views

@api_views('GET', 'POST')
def drink_list(req):
    # get all the drinks
    # serialize them
    # return json

    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks': serializer.data})