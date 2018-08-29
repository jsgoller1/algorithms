SHELL:=/bin/bash
PWD:=`pwd`

docker:
	docker run \
	-dt \
	--name python3 \
	-v $(PWD):/hackerrank \
	library/python:3

shell:
	docker exec -it python3 /bin/bash

test:
	python hr_bfs.py

solution:
	cat bfs_input | python hr_bfs.py > bfs_actual

diff:
	diff bfs_actual bfs_expected
