from django_grpc_framework  import proto_serializers
from dealership.models import Car
from car_proto import car_pb2

class CarProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Car
        proto_class = car_pb2.Car
        fields = ['id', 'brand', 'release_year', 'color']