PWD:= `pwd`

## The name of the exercise being compiled; this is
## also the dir name.
EXERCISE= `basename $$PWD`

## Name of the Docker container once started
CONTAINER_NAME:=programming-problems-workspace

## Top-level directory within the container
ROOT_DIR:=/$(CONTAINER_NAME)

## Name of git-excluded directory where binaries are built; this is
## intentionally not called "bin" to avoid accidentally crushing
## your system's /bin
BUILD_DIR:=$(ROOT_DIR)/bins
