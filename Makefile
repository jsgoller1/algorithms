##############################################################
### Dockerized Linux workspace for consistent environment. ###
### Everything in this repo is supported only within the   ###
### container environment																   ###
##############################################################

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
	--privileged \
	--name $(CONTAINER_NAME) \
	-v `pwd`:/$(CONTAINER_NAME) \
	$(CONTAINER_NAME)

# Create running shell session inside container
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# All-in-one command to build and start workspace.
workspace: docker-clean image docker shell


