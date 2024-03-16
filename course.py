class Course(object):
	course_list = list()
	
	def __init__(self, id: str, name: str, credit: int):
		self.id = id
		self.name = name
		self.credit = credit

	def toString(self):
		return f"ID: {self.id}, Name: {self.name}, Credit: {self.credit}"