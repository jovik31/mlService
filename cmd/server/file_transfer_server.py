from proto.python_grpc import file_service_pb2_grpc as file_service
from proto.python_grpc import file_service_pb2 as file_message
import grpc
import concurrent.futures as future


def get_file_bytes(filename):
    file = open(filename, 'rb')
    byteFile = file.read()
    return byteFile


def save_file(filename):


def file_server():
    server = grpc.server(future.ThreadPoolExecutor(max_workers=1))
    file_service.add_FileTranferServicer_to_server(File_Transfer(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    server.wait_for_termination()


class File_Transfer(file_service.FileTranferServicer):

    def Download(self, request, context):
        fileN = request.fileName
        print("Got request for file" + str(request.fileName))
        return file_message.File(file=get_file_bytes(request.fileName), filename=fileN)

    def DownloadStreamm(self, request_iterator, context):
        pass

    def Upload(self, request, context):
        file = request.file
        print(file)
        return file_message.ResponseFile(fileName="qwerty.csv", result="ok")

        pass

    def UploadStream(self, request_iterator, context):
        pass


file_server()
