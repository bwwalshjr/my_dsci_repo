#Assignment 1

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
		return list
	curr_list = powerset(list[1:])
	list.append(curr_list)
	return [curr_list + list[:-1]]
	
	
	
#def all_perms(list):
	

#def spiral(n, end_corner):