class Student(object):
	student_list = list()

	def __init__(self, id: str, name: str, dob: str,
				gpa: float = 0.0, mark: dict = {}):
		self.id = id
		self.name = name
		self.dob = dob
		self.gpa = gpa
		self.mark = mark

	def __str__(self):
		return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa}"

	def toString(self):
		mark_str = ""
		for key in self.mark:
			mark_str += f",{key},{self.mark[key]}"
		return f"{self.id},{self.name},{self.dob},{self.gpa}{mark_str}"

	def change_mark(self, course_id, mark):
		self.mark[course_id] = mark

	def add_to_list(self) -> str:
		for obj in Student.student_list:
			if obj.id == self.id:
				return "This student already exists!"
				
		Student.student_list.append(self)
		Student.student_list = sorted(Student.student_list, key = lambda x: x.id)
		return "Add student successful!"