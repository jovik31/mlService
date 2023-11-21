from proto.python_grpc import file_service_pb2_grpc as file_service
from proto.python_grpc import file_service_pb2 as file_message
import grpc
from cmd.internal import utils


def get_file_bytes(filename):
    file = open(filename, 'rb')
    byteFile = file.read()
    return byteFile


class FileClient:
    def __init__(self, ipAddress):
        channel = grpc.insecure_channel(ipAddress)
        self.stub = file_service.FileTranferStub(channel)

    def Download(self, file_name):

        message = file_message.Request(fileName=file_name)
        response_iterator = self.stub.Download(message)
        received_bytes = bytes()

        for response in response_iterator:
            received_bytes += response.file

        return received_bytes

    def Upload(self, file_name):

        message = utils.chunk_file(file_name, 4000000)

        self.stub.Upload(message)


client = FileClient('127.0.0.1:50051')
client.Upload("tranco_3VPWL.csv")

# response = client.Download('tranco_3VPWL.csv')
# utils.response_to_csv(response, 'domains.csv')
