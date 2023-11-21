from proto.python_grpc import file_service_pb2 as file_message


def response_to_csv(response, file_name):
    string_response = response.decode("utf-8")
    file = open(file_name, 'w')
    file.write(string_response)


def chunk_file(file_name, chunk_size):

    index = 0
    file = open(file_name, 'rb')
    byte_file = file.read()

    while index < len(byte_file):

        yield file_message.File(file=byte_file[index:index+chunk_size])

        index += chunk_size
