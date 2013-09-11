#!/usr/bin/python

def function(elem, lfunct):
    return [funct(elem) for funct in lfunct]
    

def add_three(elem):
	return elem + 3

def mul_five(elem):
	return elem * 5
	
def subtract_two(elem):
    return elem - 2

if __name__ == "__main__":
	list = []
	list.append(add_three)
	list.append(mul_five)
	list.append(subtract_two)
	
	number = raw_input('Choose an integer : ')
	
	l = []
	l = function(int(number), list)
	print l
