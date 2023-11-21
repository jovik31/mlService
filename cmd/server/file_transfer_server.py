from proto.python_grpc import file_service_pb2_grpc as file_service
from proto.python_grpc import file_service_pb2 as file_message
import grpc
import concurrent.futures as future
from cmd.internal import utils


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
        return utils.chunk_file(fileN, 4000000)

    def Upload(self, request_iterator, context):

        print("got to server")

        uploaded_file = bytes()
        for requests in request_iterator:
            uploaded_file += requests.file

        print(uploaded_file.decode("utf-8"))
        return file_message.Response(fileName="eeee.csv", result="ok")


file_server()
