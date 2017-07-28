class Node(object):

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __repr__(self):
		return repr(self.data)


class SinglyLinkedList(Node):

	def __init__(self):
		self.head = None

	def __repr__(self):
		curr = self.head
		nodes = []
		while curr:
			nodes.append(repr(curr))
			curr = curr.next
		return '[' + ', '.join(nodes) + ']'

	def prepend(self, data):
		self.head = Node(data, self.head)

	def append(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(data)

	def search(self, data):
		curr = self.head
		while curr and curr.data != data:
			curr = curr.next
		return curr

	def delete(self, data):
		curr = self.head
		prev = None
		while curr and curr.data != data:
			prev = curr
			curr = curr.next
		if prev == None:
			self.head = curr.next
		else:
			prev.next = curr.next
			curr.next = None

	def reverse(self):
		curr = self.head
		next_node = None
		prev_node = None

		while curr:
			next_node = curr.next
			curr.next = prev_node
			prev_node = curr
			curr = next_node
		self.head = prev_node
