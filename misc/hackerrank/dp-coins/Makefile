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
	python dp_coins.py

solution:
	cat dp_coins | python dp_coins.py > bfs_actual

diff:
	diff bfs_actual bfs_expected
