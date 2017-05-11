
class BinarySearch(list):
	"init method with a as the length of list and b as the step of elements in the array"
	def __init__(self, a, b):
		"creates a list of a length with b spacing between the elements"

		for i in range(1, a+1):
			self.append(i * b)

		self.length = len(self)

	"""search method implementing binary search algorithm with 
	   the parameter value as the element to be searched for
	"""
	def search(self, myItem):

		self.counter = 0
		self.found = False
		self.bottom = 0
		self.index = 0
		self.top = len(self)-1

		"finds out if value is the first or last element in the list"

		if myItem == self[self.bottom]:
			self.index = first
			self.found = True
		elif myItem == self[self.top]:
			self.index = self.top
			self.found = True

		"determines if value is not in the list"

		if myItem not in self:
			return {"count": self.counter, "index": -1}

		"""The binary search algorithm. Finds the middle number 
		   in list and determines if it is equal to the value 
		   being searched for.
        """
		while self.bottom <= self.top and not self.found:
			self.middle = (self.bottom + self.top)//2
			if self[self.middle] == myItem:
				self.found = True
				self.index = self.middle
			else:
				self.counter += 1
				if self[self.middle] < myItem:
					self.bottom = self.middle + 1	
				else:
					self.top = self.middle - 1

		
		if self.found:    
			self.result = {"count": self.counter, "index": self.index}
		else:
			self.result = {"count": self.counter, "index": -1}

		return self.result




z = BinarySearch(20,2)
print z
print z.search(19)

