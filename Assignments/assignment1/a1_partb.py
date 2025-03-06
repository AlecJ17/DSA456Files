#    Main Author(s): Alec Josef Serrano/ Duc Phu Nguyen
#    Main Reviewer(s):



class SortedList:
	class Node:
		def __init__(self, data, next=None, prev=None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self):
		self.front = None
		self.back = None
		self.size = 0  # Initialize size to 0

	def get_front(self):
		return self.front

	def get_back(self):
		return self.back

	def is_empty(self):
		return self.size == 0  # Return True if size is 0, False otherwise

	def __len__(self):
		return self.size  # Return the size

	def insert(self, data):
		nn = self.Node(data)
		if self.is_empty():
			self.front = self.back = nn
		else:
			curr = self.front
			while curr is not None and curr.get_data() < data:
				curr = curr.get_next()
			if curr is None:  # data is biggest number in SortedList => push_back
				nn.prev = self.back
				self.back.next = nn
				self.back = nn
				nn.next = None
			elif curr == self.front:  # data is smallest number in SortedList => push_front
				nn.next = self.front
				self.front.prev = nn
				self.front = nn
				nn.prev = None
			else:  # data is between numbers in SortedList insert(curr)
				prev_Node = curr.prev
				nn.next = curr
				nn.prev = prev_Node
				if prev_Node is not None:
					prev_Node.next = nn
				curr.prev = nn
		self.size += 1  # Increment size
		return nn

	def erase(self, node):
		# Checks if the node is none
		if node is None:
			raise ValueError('Cannot erase node referred to by None')
		# Checks if the node is the Front Node
		if node == self.front:
			self.front = node.next
			if self.front:
				self.front.prev = None
		# Checks if the node is not the front node
		else:
			if node.prev:
				node.prev.next = node.next
			if node.next:
				node.next.prev = node.prev
			if node == self.back:
				self.back = node.prev
		self.size -= 1  # Decrement size
		if self.size == 0:  # If list is empty, reset front and back
			self.front = self.back = None

	def search(self, data):
		current = self.front
		while current:
			if current.data == data:
				return current
			current = current.next
		return None
