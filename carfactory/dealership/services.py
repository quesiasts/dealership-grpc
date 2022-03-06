import grpc
from google.protobuf import empty_pb2
from django_grpc_framework.services import Service
from dealership.models import Car
from dealership.serializers import CarProtoSerializer

class CarService(Service):
    def List(self, request, context):
        cars = Car.objects.all()
        serializer = CarProtoSerializer(cars, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = CarProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post: %s not found!' % pk)

    def Retry(self, request, context):
        car = self.get_object(request.id)
        serializer = CarProtoSerializer(car)
        return serializer.message

    def Update(self, request, context):
        car = self.get_object(request.id)
        serializer = CarProtoSerializer(car, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        car = self.get_object(request.id)
        car.delete()
        return empty_pb2.Empty()        
