CONTAINER_NAME:=programming-problems-workspace
ROOT_DIR:=/$(CONTAINER_NAME)

### Uncomment this to run Clang's static analyzer while building; this makes the build slower.
ANALYZER:=scan-build --status-bugs

### Compiler settings
CC:=clang++
CFLAGS :=-std=c++17 -g -lm
WARNINGS :=-Weverything -Werror
COMPILE:=$(ANALYZER) $(CC) $(CFLAGS) $(WARNINGS)

### Valgrind target for memory analysis
VALGRIND := valgrind -q --leak-check=full --show-leak-kinds=all --track-origins=yes --error-exitcode=42

### Binary cleanup
setup:
	-mkdir $(ROOT_DIR)/bin

clean:
	-rm -r $(ROOT_DIR)/bin/*

clear:
	clear

#############################################################
### Dockerized Linux workspace for consistent environment ###
#############################################################

# Remove existing containers
docker-clean:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)

# Build image from Dockerfile
image:
	-docker pull ubuntu
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


