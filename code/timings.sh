#!/bin/bash

echo Timing: ON
printf "\n"


echo Cliquet HIGH
echo ============
for m in $(seq 1000)
do
	python -m timeit -u sec -s "from runCliquet import run_cliquet_high" "run_cliquet_high([$m])"
done
printf "\n"

echo Cliquet LOW
echo ===========
for m in $(seq 1000)
do
	python -m timeit -s "from runCliquet import run_cliquet_low" "run_cliquet_low([$m])"
done
printf "\n"

echo Cliquet VAR
echo ===========
for m in $(seq 1000)
do
	python -m timeit -s "from runCliquet import run_cliquet_var" "run_cliquet_var([$m])"
done
printf "\n"


# echo Asian Table 2 sigma=0.2
# echo =======================
# for m in 50 100 200 400 800
# do
	# echo m = $m
	# python -m timeit -u sec -s "from runAsian import run_asian" "run_asian([$m])"
	# echo ----------------------------------------
# done
# printf "\n"


echo Timing: OFF
