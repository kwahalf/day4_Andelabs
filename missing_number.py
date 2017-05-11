"function that compares two arrays and retuns values not common to both"
def find_missing(list_A, list_B):
	"creates a new list that combines the two lists"
	list_C = list_A + list_B
	"generates a new list to be iterated over by combining the two list"
	list_D = []
	if list_C == []:
		return 0
		"retuns 0 if the compared lists are both empty"
	elif list_A == list_B:
		return 0
		"returns  0 if lists are similar"

	elif (len(list_B) -len(list_A) == 1):
		for element in list_C:
			"check for element not apearing in bothe the list"
			if element not in list_A or element not in list_B:
				return  element 
				continue


	else:
		for element in list_C:
			"check for elements not apearing in bothe the list"
			if element not in list_A or element not in list_B:
				list_D.append(element) 
				continue
				
		return list_D

