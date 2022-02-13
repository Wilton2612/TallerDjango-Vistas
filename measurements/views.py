
from .logic import measurements_logic as mr
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = mr.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurement_dto = mr.get_measurements()
            measurements = serializers.serialize('json', measurement_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        measurement_dto = mr.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = mr.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement , 'application/json')

    if request.method == 'PUT':
        measurement_dto = mr.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'DELETE':
        measurement_dto = mr.delete_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')