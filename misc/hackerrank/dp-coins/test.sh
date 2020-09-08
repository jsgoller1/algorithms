#!/bin/bash

AMOUNTS=`seq 1 50`

for AMOUNT in $AMOUNTS; do
	printf "$AMOUNT 4\n1 5 10 25" | python coin_solution_obfuscated.py;
done
