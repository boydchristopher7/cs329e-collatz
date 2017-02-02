#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
	"""
	read two ints
	s a string
	return a list of two ints, representing the beginning and end of a range, [i, j]
	"""
	a = s.split()
	return [int(a[0]), int(a[1])]

# ------------
# make_cache
# ------------

global cache
cache = []

def make_cache():
	cache_increment = 10000
	cache.append(collatz_eval((len(cache)*cache_increment)+1, (len(cache)+1)*cache_increment))


# ------------
# collatz_eval
# ------------

def collatz_eval(i, j):
	"""
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	return the max cycle length of the range [i, j]
	"""
	if i > j:
		i, j = j, i
		
	max_cycle = 0
	for each in range(i, j + 1):
		temp = each
		cycle = 1
		while temp > 1:
			if temp % 2 == 0:
				temp = temp / 2
			else:
				temp = temp * 3
				temp += 1

			cycle += 1

		if cycle > max_cycle:
			max_cycle = cycle

	return max_cycle


# -------------
# collatz_print
# -------------

def collatz_print(w, i, j, v):
	"""
	print three ints
	w a writer
	i the beginning of the range, inclusive
	j the end       of the range, inclusive
	v the max cycle length
	"""
	w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
	"""
	r a reader
	w a writer
	"""
	for s in r:
		i, j = collatz_read(s)
		v = collatz_eval(i, j)
		collatz_print(w, i, j, v)