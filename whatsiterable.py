class counting:
	
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __iter__(self):
		return self
	
	def __next__(self, current, end):
		if self.current >= self.start:
			return self.current+2
			val = self.current+2
			self.current
			return val
		
		
for i in range(0,20):
	print(i)
