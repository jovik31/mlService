run:
	python3 cmd/server/server.py


gen:
	python3 -m grpc_tools.protoc --proto_path=./proto/ --python_out=./proto/python_grpc --go_out=./proto --grpc_python_out=./proto/python_grpc --go-grpc_out=./proto proto/file_service.proto

clean:
	rm proto/python_grpc/*.py proto/go_grpc/*go
	touch proto/python_grpc/__init__.py
set-env:
	export PYTHONPATH=~/Projects/pyProjects/mlService/
