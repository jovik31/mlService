import file_service_pb2_grpc as file_grpc
import file_service_pb2 as file_pb
import log


class File_Transfer(file_grpc.FileTransferServicer):

    pass


def Upload(self, request, context):
    log.info("Upload requested")
    log.info(f"Requested - {request}")
