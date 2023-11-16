run:
	python3 cmd/server/server.py


gen:
	python3 -m grpc_tools.protoc --proto_path=. proto/file_service.proto --python_out=./proto/python --go_out=./proto/go --grpc_python_out=./proto/python --go-grpc_out=./proto/go


clean:
	rm proto/python/proto/*.py proto/go/proto/*go
