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

p = int(raw_input())
q = int(raw_input())
total = 0;
for number in range(p, q+1):
    if Kaprecar(number):
        print number,
        total = 1
if total == 0:
    print "INVALID RANGE"