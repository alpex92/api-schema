.PHONY: docs java swagger gateway python2 python3 php golang

PROJECT_PATH   := $(shell pwd)
PROTO_PATH     := $(PROJECT_PATH)/proto
JAVA_GEN_PATH  := $(PROJECT_PATH)/java
PHP_GEN_PATH   := $(PROJECT_PATH)/php
DOCS_PATH      := $(PROJECT_PATH)/docs
SWAGGER_PATH   := $(PROJECT_PATH)/swagger
HTTP_GW_PATH   := $(PROJECT_PATH)/http_gateway
GOLANG_PATH    := $(PROJECT_PATH)/golang
PYTHON2_PATH   := $(PROJECT_PATH)/python2
PYTHON3_PATH   := $(PROJECT_PATH)/python3

python2:
	mkdir -p $(PYTHON2_PATH)
	docker run --name py_grpc_builder -d -i -t \
	-v $(PROJECT_PATH):/project \
	-v $(GOPATH):/go \
	-v $(PYTHON2_PATH):/out \
	-w /project \
	python:latest bash
	docker exec -it -w /project py_grpc_builder bash scripts/py2.sh
	docker rm -f py_grpc_builder

python3:
	mkdir -p $(PYTHON3_PATH)
	docker run --name py_grpc_builder -d -i -t \
	-v $(PROJECT_PATH):/project \
	-v $(GOPATH):/go \
	-v $(PYTHON3_PATH):/out \
	-w /project \
	python:latest bash
	docker exec -it -w /project py_grpc_builder bash scripts/py3.sh
	docker rm -f py_grpc_builder

java:
	mkdir -p $(JAVA_GEN_PATH)
	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	--plugin=protoc-gen-grpc-java=opt/protoc-gen-grpc-java-1.13.2-osx-x86_64.exe \
  --grpc-java_out="$(JAVA_GEN_PATH)" \
	--java_out="$(JAVA_GEN_PATH)" \
	$(PROTO_PATH)/*.proto

	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	--java_out="$(JAVA_GEN_PATH)" \
	include/scalapb/scalapb.proto

php:
	mkdir -p $(PHP_GEN_PATH)
	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	--php_out=$(PHP_GEN_PATH) \
	$(PROTO_PATH)/*.proto

swagger:
	mkdir -p $(SWAGGER_PATH)
	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	-I/usr/local/include \
	-I$(GOPATH)/src \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	--swagger_out=logtostderr=true:$(SWAGGER_PATH) \
	$(PROTO_PATH)/*.proto

golang:
	mkdir -p $(GOLANG_PATH)
	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	--go_out=\
	Mgoogle/protobuf/descriptor.proto=github.com/golang/protobuf/protoc-gen-go/descriptor,\
	Mscalapb/scalapb.proto=github.com/gogo/protobuf/types,\
	plugins=grpc:$(GOLANG_PATH) \
	$(PROTO_PATH)/*.proto
	
	@PATH=$(PATH):$(CWD) protoc -I$(PROTO_PATH) \
	-Iinclude \
	-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
	--gosdk_out=$(GOLANG_PATH) \
	$(PROTO_PATH)/*.proto

docs:
	rm -rf $(DOCS_PATH)
	mkdir -p $(DOCS_PATH)
	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	--plugin=protoc-gen-doc=$(GOPATH)/bin/protoc-gen-doc \
	--doc_out=$(DOCS_PATH) \
	--doc_opt=markdown,readme.md \
	$(PROTO_PATH)/*.proto

	@protoc -I$(PROTO_PATH) \
	-Iinclude \
	--plugin=protoc-gen-doc=$(GOPATH)/bin/protoc-gen-doc \
	 --doc_out=$(DOCS_PATH) \
	--doc_opt=html,index.html \
	$(PROTO_PATH)/*.proto
