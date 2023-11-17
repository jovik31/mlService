from proto.python_grpc import file_service_pb2_grpc as file_service
from proto.python_grpc import file_service_pb2 as file_message
import grpc


class FileClient:
    def __init__(self, ipAddress):
        channel = grpc.insecure_channel(ipAddress)
        self.stub = file_service.FileTranferStub(channel)

    def Download(self, fileName):


channel = grpc.insecure_channel('127.0.0.1:50051')
stub = file_service.FileTranferStub(channel)
response = stub.Download(file_message.RequestFile(fileName="wert.csv"))

print(response)
