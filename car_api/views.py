from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Manufacturer, CarModel, Car
from .serializers import ManufacturerSerializer



@api_view(['POST','GET'])
def carEndPoint(request):
    if request.method == 'GET':
        try:
            name = request.query_params['name']
            query_set = Manufacturer.objects.filter(name=name).prefetch_related(
                'carmodel_set')

            sequalizer = ManufacturerSerializer(query_set, many=True)
            return Response(sequalizer.data)
        except Exception as err:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Car created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)