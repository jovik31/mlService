from proto.python_grpc import file_service_pb2_grpc as file_service
from proto.python_grpc import file_service_pb2 as file_message
import grpc


def get_file_bytes(filename):
    file = open(filename, 'rb')
    byteFile = file.read()
    return byteFile


def chunk_file(filename):
    pass


class FileClient:
    def __init__(self, ipAddress):
        channel = grpc.insecure_channel(ipAddress)
        self.stub = file_service.FileTranferStub(channel)

    def Download(self, file_name):
        response = self.stub.Download(
            file_message.RequestFile(fileName=file_name))
        return response

    def Upload(self, file_name):
        response = self.stub.Upload(file_message.File(
            file=get_file_bytes(file_name), filename=file_name))
        return response

    def DownloadStream(self, file_name):
        pass

    def UploadStream(self, file_name):

        pass


client = FileClient('127.0.0.1:50051')
response = client.Download('wert.csv')
print(response)
