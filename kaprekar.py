#!/usr/bin/python
# -*- coding: utf-8 -*-

def Kaprecar(nb):
    square = nb * nb
    str_square = str(square)
    half_one, half_two = str_square[:len(str_square)/2], str_square[len(str_square)/2:]
    if (square < 10):
        half_one = '0'
    if (int(half_one) + int(half_two) == nb) :
        return True
    return False


if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
elif len(sys.argv) == 1:
    start = 1
    end = 100
else:
    print "Usage ./kaprecar.py [start end]"
    exit(0)

total = 0;
for number in range(start, end+1):
    if Kaprecar(number):
        print number,
        total = 1
if total == 0:
    print "INVALID RANGE"