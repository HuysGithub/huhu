import os
from multiprocessing import Process
import tkinter as tk
from tkinter import Label, Entry
import zipfile

from student import Student
from course import Course

def compress():
	with zipfile.ZipFile("student.dat", "a", compression=zipfile.ZIP_LZMA) as zipf:
		zipf.write("students.txt")
	os.remove("students.txt")
def decompress():
	if os.path.exists("student.dat") and zipfile.is_zipfile("student.dat"):
		with zipfile.ZipFile("student.dat") as zipf:
			zipf.extractall()
		os.remove("student.dat")

def load_student():
	if os.path.exists("students.txt"):
		with open("students.txt","r") as reader:
			for line in reader:
				path = line.strip().split(",")
				mark = {}
				for i in range(4, len(path),2):
					mark[path[i]] = float(path[i+1])
				student = Student(path[0], path[1], path[2], path[3], mark)
				Student.student_list.append(student)

def save_student():
	with open("students.txt", "w") as writer:
		for student in Student.student_list:
			writer.write(student.toString() + "\n")

def onclick_addStudent():
	sub = tk.Toplevel(window)
	sub.title("ADD STUDENT")
	sub.geometry("300x300")
	id_label = Label(sub, text="ID")
	id_label.pack()
	id_entry = Entry(sub)
	id_entry.pack()
	fullname_label = Label(sub, text="Full Name")
	fullname_label.pack()
	fullname_entry = Entry(sub)
	fullname_entry.pack()

	dob_label = Label(sub, text="DoB")
	dob_label.pack()
	dob_entry = Entry(sub)
	dob_entry.pack()
	button_OK = tk.Button(sub,text="OK", command=lambda:on_click_OK())
	button_OK.pack()
	button_exit = tk.Button(sub, text="Exit", command=sub.destroy)
	button_exit.pack()
	notice = Label(sub, text="")
	notice.pack()

	def on_click_OK():
		id = id_entry.get()
		name = fullname_entry.get()
		dob = dob_entry.get()
		student = Student(id,name,dob)
		notice_detail = student.add_to_list()
		notice.config(text=notice_detail)

def onclick_showStudent():
	sub = tk.Toplevel()
	sub.title("Student Information")
	table_label = Label(sub)
	id_label = Label(table_label)
	id_txt = Label(id_label, text="ID")
	id_txt.pack()
	for student in Student.student_list:
		stid_label = Label(id_label, text=student.id)
		stid_label.pack()
	id_label.grid(row=0,column=0)

	name_label = Label(table_label)
	name_txt = Label(name_label, text="Name")
	name_txt.pack()
	for student in Student.student_list:
		stname_label = Label(name_label, text=student.name)
		stname_label.pack()
	name_label.grid(row=0,column=1)

	table_label.pack()

if __name__ == "__main__":
	decompress()
	p = Process(target=load_student())
	p.start()
	p.join()

	window = tk.Tk()
	window.geometry("300x300")

	window.title("Hospital management")
	student_label = Label(window)
	button_addStudent = tk.Button(student_label, text="ADD STUDENT", command=lambda: onclick_addStudent())
	button_addStudent.grid(row=0, column=0)
	button_showStudent = tk.Button(student_label, text="SHOW STUDENT", command=lambda: onclick_showStudent())
	button_showStudent.grid(row=0, column=1)
	student_label.pack()
	# id = input("ID: ")
	# name = input("Name: ")
	# dob = input("DoB: ")
	# student = Student(id,name,dob)
	# student.add_to_list()

	# for student in Student.student_list:
	# 	print(student)
	
	window.mainloop()
	save_student()
	compress()