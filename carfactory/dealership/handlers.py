from dealership.services import CarService
from car_proto import car_pb2_grpc

def grpc_handlers(server):
    car_pb2_grpc.add_CarControllerServicer_to_server(CarService.as_servicer(), server)