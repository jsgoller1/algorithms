CONTAINER_NAME:=programming-problems-workspace

### Uncomment this to run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

### Compiler settings
CC:=clang
CFLAGS :=-std=gnu11 -g -lm -pthread
WARNINGS :=-Weverything -Werror
INCLUDES :=-I common/include
LIBS := common/src/*.c
EXTRA_FLAGS:=-D TEST_OUTPUT
COMPILE:=$(ANALYZER) $(CC) $(CFLAGS) $(WARNINGS) $(EXTRA_FLAGS)

### Valgrind target for memory analysis
VALGRIND := valgrind -q --leak-check=full --show-leak-kinds=all --track-origins=yes --error-exitcode=42

### Binary cleanup
setup:
	-mkdir bin

clean:
	-rm -r bin/*

#############################################################
### Dockerized Linux workspace for consistent environment ###
#############################################################

# Remove existing containers
docker-clean:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

# Build image from Dockerfile
image:
	docker pull ubuntu
	docker build . -t $(CONTAINER_NAME)

# Start running container from built image
docker:
	docker run \
	-dt \
	--name $(CONTAINER_NAME) \
	-v `pwd`:/$(CONTAINER_NAME) \
	$(CONTAINER_NAME)

# Create running shell session inside container
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# All-in-one command to build and start workspace.
workspace: docker-clean image docker shell


