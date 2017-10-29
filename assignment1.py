#Assignment 1
#Author: Brian Walsh

def flatten(list_name):
	for elem in list_name: #iterate through list
		if isinstance(elem, list):
			list_name.extend(elem)
			list_name.remove(elem)
	if not any(isinstance(element, list) for element in list_name):
		return list_name
	else:
		return flatten(list_name)

def powerset(list):
	if len(list) == 0: 
		return [[]]
	tail = powerset(list[1:]) 
	return tail + [[list[0]] + element for element in tail]

def all_perms(list):
	if len(list) == 1:
		return [list]
	empty_list = []
	for index in range(len(list)):
		solo_list = [list[index]]
		for mini_list in all_perms(list[:index] + list[index+1:]):
			empty_list.append(solo_list + mini_list)
	return empty_list

def spiral(n, ec):
	def down(coord):
		return [coord[0], coord[1] + 1]
	def left(coord):
		return [coord[0] - 1, coord[1]]
	def right(coord):
		return [coord[0] + 1, coord[1]]
	def up(coord):
		return [coord[0], coord[1] - 1]
	def can_down(n, coord, matrix):
		if coord[1] + 1 < n and matrix[coord[1] + 1][coord[0]] == 0:
			return True
		return False
	def can_left(n, coord, matrix):
		if coord[0] - 1 >= 0 and matrix[coord[1]][coord[0] - 1] == 0:
			return True
		return False
	def can_right(n, coord, matrix):
		if coord[0]+1 < n and matrix[coord[1]][coord[0] + 1] == 0:
			return True
		return False
	def can_up(n, coord, matrix):
		if coord[1] - 1 >= 0 and matrix[coord[1] - 1][coord[0]] == 0:
			return True
		return False

	matrix = [[0 for i in xrange(n)] for i in xrange(n)]
	snum = n*n - 1

	if ec == 1:
		start = [0, 0]
		matrix[start[1]][start[0]] = snum
		coord = start
		while(snum != 0):
			while (can_down(n, coord, matrix)) and snum != 0:
				coord = down(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_right(n, coord, matrix)) and snum != 0:
				coord = right(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_up(n, coord, matrix)) and snum != 0:
				coord = up(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_left(n, coord, matrix)) and snum != 0:
				coord = left(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum		
	if ec == 2:
		start = [n - 1, 0]
		matrix[start[1]][start[0]] = snum
		coord = start
		while(snum != 0):
			while(can_left(n, coord, matrix)) and snum != 0:
				coord = left(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_down(n, coord, matrix)) and snum != 0:
				coord = down(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_right(n, coord, matrix)) and snum != 0:
				coord = right(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_up(n, coord, matrix)) and snum != 0:
				coord = up(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum		
	if ec == 3:
		start = [0, n-1]
		matrix[start[1]][start[0]] = snum
		coord = start
		while(snum != 0):
			while(can_right(n, coord, matrix)) and snum != 0:
				coord = right(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_up(n, coord, matrix)) and snum != 0:
				coord = up(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_left(n, coord, matrix)) and snum != 0:
				coord = left(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_down(n, coord, matrix)) and snum != 0:
				coord = down(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum		
	if ec == 4:
		start = [n-1, n-1]
		matrix[start[1]][start[0]] = snum
		coord = start
		while(snum != 0):
			while(can_up(n, coord, matrix)) and snum != 0:
				coord = up(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_left(n, coord, matrix)) and snum != 0:
				coord = left(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_down(n, coord, matrix)) and snum != 0:
				coord = down(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
			while(can_right(n, coord, matrix)) and snum != 0:
				coord = right(coord)
				snum = snum - 1
				matrix[coord[1]][coord[0]] = snum
				
	for line in matrix:
		print line
	return ("Printed")