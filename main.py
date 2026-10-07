import json
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data) -> Car:
    if isinstance(json_data, bytes):
        json_data = json_data.decode("utf-8")

    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
