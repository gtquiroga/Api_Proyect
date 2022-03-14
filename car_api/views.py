from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Manufacturer, CarModel, Car
from .serializers import ManufacturerSerializer, CarModelSerializer


@api_view(['POST','GET'])
def carEndPoint(request):
    if request.method == 'GET':
        name = request.query_params['name']
        query_set = Manufacturer.objects.filter(name=name).prefetch_related(
            'carmodel_set')

        sequalizer = ManufacturerSerializer(query_set, many=True)
        return Response(sequalizer.data)

    elif request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)